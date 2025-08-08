import time
import random
from datetime import datetime
from collections import deque
from multiprocessing import Process, Pipe, Queue, Event, set_start_method, freeze_support
import numpy as np
import hashlib
import json
def calc_hash(prev_hash: str, datos: dict, timestamp: str) -> str:
    payload = prev_hash + json.dumps(datos, sort_keys=True) + timestamp
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

# ---------------- ANALIZADOR GENÉRICO ---------------- #
def analyzer(tipo, conn, queue_out, stop_evt):
    ventana = deque(maxlen=30)
    while not stop_evt.is_set():
        try:
            pkt = conn.recv()
            if pkt is None:
                break

            if tipo == "frecuencia":
                valor = pkt["frecuencia"]
            elif tipo == "presion":
                valor = (pkt["presion"][0], pkt["presion"][1])  # Sistolica y diastolica
            elif tipo == "oxigeno":
                valor = pkt["oxigeno"]
            else:
                continue

            ventana.append(valor)
            datos = np.array(ventana, dtype=float)
            if tipo == "presion":
                sistolicas = [v[0] for v in ventana]
                diastolicas = [v[1] for v in ventana]
                queue_out.put({
                    "tipo": tipo,
                    "timestamp": pkt["timestamp"],
                    "media": {
                        "sistolica": round(np.mean(sistolicas), 2),
                        "diastolica": round(np.mean(diastolicas), 2)
                    },
                    "desv": {
                        "sistolica": round(np.std(sistolicas, ddof=0), 2),
                        "diastolica": round(np.std(diastolicas, ddof=0), 2)
                    }
                })
                continue  # Saltear el envío genérico
            queue_out.put({
                "tipo": tipo,
                "timestamp": pkt["timestamp"],
                "media": round(datos.mean(), 2),
                "desv": round(datos.std(ddof=0), 2)
            })
        except EOFError:
            break
    conn.close()

# ---------------- GENERADOR DE DATOS ---------------- #
def generar_muestra():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "frecuencia": random.randint(60, 180),
        "presion": [random.randint(110, 180), random.randint(70, 110)],
        "oxigeno": random.randint(90, 100)
    }

def verifier(queue_in, total_samples, path_out):
    blockchain = []
    results_by_ts = {}
    prev_hash = "0" * 64
    completados = 0
    fins = 0

    while completados < total_samples:
        data = queue_in.get()
        if data.get("tipo") == "FIN":
            fins += 1
            if fins == 3:
                break
            continue

        ts = data["timestamp"]
        tipo = data["tipo"]
        results_by_ts.setdefault(ts, {})
        results_by_ts[ts][tipo] = {"media": data["media"], "desv": data["desv"]}

        if {"frecuencia", "presion", "oxigeno"} <= results_by_ts[ts].keys():
            f = results_by_ts[ts]["frecuencia"]["media"]
            p = results_by_ts[ts]["presion"]["media"]["sistolica"]
            o = results_by_ts[ts]["oxigeno"]["media"]

            alerta = not (f < 200 and 90 <= o <= 100 and p < 200)

            bloque = {
                "timestamp": ts,
                "datos": results_by_ts[ts],
                "alerta": alerta,
                "prev_hash": prev_hash,
                "hash": None
            }

            bloque["hash"] = calc_hash(prev_hash, bloque["datos"], ts)
            blockchain.append(bloque)
            prev_hash = bloque["hash"]
            completados += 1
            print(f"[BLOQUE #{completados}] hash={bloque['hash'][:12]}... alerta={alerta}")
            del results_by_ts[ts]

            with open(path_out, "w", encoding="utf-8") as f:
                json.dump(blockchain, f, indent=2)

# ---------------- PROGRAMA PRINCIPAL ---------------- #
def main():
    freeze_support()
    try:
        set_start_method("spawn")
    except RuntimeError:
        pass

    # Pipes para comunicación
    pA_hijo, pA_padre = Pipe(duplex=False)
    pB_hijo, pB_padre = Pipe(duplex=False)
    pC_hijo, pC_padre = Pipe(duplex=False)

    queue_resultados = Queue()
    stop_event = Event()

    # Enviar 60 muestras
    TOTAL = 60
    path_blockchain = "blockchain.json"
    # Crear proceso verificador
    V = Process(target=verifier, args=(queue_resultados, TOTAL, path_blockchain))

    # Crear procesos analizadores
    A = Process(target=analyzer, args=("frecuencia", pA_hijo, queue_resultados, stop_event))
    B = Process(target=analyzer, args=("presion",    pB_hijo, queue_resultados, stop_event))
    C = Process(target=analyzer, args=("oxigeno",    pC_hijo, queue_resultados, stop_event))

    A.start(); B.start(); C.start()
    V.start()

    try:
        for _ in range(TOTAL):
            pkt = generar_muestra()
            pA_padre.send(pkt)
            pB_padre.send(pkt)
            pC_padre.send(pkt)
            time.sleep(1)
    finally:
        for p in (pA_padre, pB_padre, pC_padre):
            p.send(None)
            p.close()
        stop_event.set()
        A.join(); B.join(); C.join()
        queue_resultados.put({"tipo": "FIN"})
        queue_resultados.put({"tipo": "FIN"})
        queue_resultados.put({"tipo": "FIN"})
        V.join()

    # Mostrar resultados
    # while not queue_resultados.empty():
    #     r = queue_resultados.get()
    #     print(f"[{r['timestamp']}] {r['tipo']} -> media={r['media']}, desv={r['desv']}")

if __name__ == "__main__":
    main()