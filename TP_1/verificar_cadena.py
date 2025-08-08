import json
import hashlib
import statistics

def calc_hash(prev_hash: str, datos: dict, timestamp: str) -> str:
    payload = prev_hash + json.dumps(datos, sort_keys=True) + timestamp
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def main():
    try:
        with open("blockchain.json", "r", encoding="utf-8") as f:
            chain = json.load(f)
    except FileNotFoundError:
        print("❌ No se encontró el archivo blockchain.json")
        return
    except json.JSONDecodeError:
        print("❌ Error al leer el archivo blockchain.json: formato inválido")
        return

    corrupt = []
    prev = "GENESIS"
    freqs, press, oxys = [], [], []
    diastolic = []
    alertas = 0

    for i, blk in enumerate(chain):
        esperado = calc_hash(prev, blk["datos"], blk["timestamp"])
        if blk["hash"] != esperado or blk["prev_hash"] != prev:
            corrupt.append(i)
        prev = blk["hash"]

        freqs.append(blk["datos"]["frecuencia"]["media"])
        press.append(blk["datos"]["presion"]["media"]["sistolica"])
        diastolic.append(blk["datos"]["presion"]["media"]["diastolica"])
        oxys.append(blk["datos"]["oxigeno"]["media"])
        if blk.get("alerta"):
            alertas += 1

    total = len(chain)
    prom_f = statistics.fmean(freqs) if freqs else 0.0
    prom_p = statistics.fmean(press) if press else 0.0
    prom_d = statistics.fmean(diastolic) if diastolic else 0.0
    prom_o = statistics.fmean(oxys) if oxys else 0.0

    lineas = [
        f"Total de bloques: {total}",
        f"Bloques con alerta: {alertas}",
        f"Promedio general frecuencia: {prom_f:.2f}",
        f"Promedio general presion (sistolica): {prom_p:.2f}",
        f"Promedio general presion (diastolica): {prom_d:.2f}",
        f"Promedio general oxigeno: {prom_o:.2f}",
        "Cadena íntegra: SIN CORRUPCIONES DETECTADAS" if not corrupt
        else "Bloques corruptos en índices: " + ", ".join(map(str, corrupt))
    ]
    txt = "\n".join(lineas)
    print(txt)
    with open("reporte.txt", "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print("✅ Verificación completa. Reporte guardado en reporte.txt")

if __name__ == "__main__":
    main()