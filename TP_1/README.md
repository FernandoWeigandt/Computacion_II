
---

# Sistema Concurrente de Análisis Biométrico con Blockchain Local

## 🧠 Descripción

Este sistema reproduce una prueba de esfuerzo biométrica, procesando señales de manera concurrente y registrando los resultados en una cadena de bloques local para garantizar su integridad.

---

## 📦 Componentes

* **`main.py`**: genera las señales, las procesa en paralelo y construye bloques validados.
* **`verificar_cadena.py`**: comprueba la consistencia de la cadena y produce un reporte final.
* **`blockchain.json`**: archivo que almacena la secuencia de bloques encadenados.
* **`reporte.txt`**: resumen con estadísticas (incluyendo presión sistólica y diastólica) y alertas detectadas.

---

## ⚙️ Modelo de procesos

Cuando se ejecuta el sistema, los procesos se organizan de la siguiente manera:

1. **Proceso principal**: actúa como coordinador general, iniciando y controlando la finalización de todos los procesos secundarios.
2. **Proceso generador**: produce un dato por segundo siguiendo el formato establecido.
3. **Procesos analizadores** (tres en total): cada uno recibe y procesa un tipo específico de dato proveniente del generador.
4. **Proceso verificador**: recopila los resultados de los analizadores, los valida y los almacena como bloques en la cadena.

Para la creación de procesos se utiliza la librería `multiprocessing` en lugar de `os`, ya que ofrece una interfaz más simple y reduce problemas frecuentes con `fork` (por ejemplo, procesos que no finalizan o no esperan correctamente a los hijos).

---

## 🔗 Comunicación entre procesos (IPC)

El sistema emplea dos mecanismos distintos según el flujo de datos:

* **Generador → Analizadores**: se utiliza un **pipe independiente para cada analizador**. Los *pipes* anónimos creados con `multiprocessing.Pipe` son preferibles en este contexto porque se generan solo entre procesos que se comunican directamente, evitando accesos externos y simplificando la implementación respecto a *named pipes* (FIFO).
* **Analizadores → Verificador**: la transmisión se realiza mediante **colas (`Queue`)**, que permiten que múltiples productores escriban en una misma estructura y un único consumidor procese la información, todo de manera segura y sincronizada.

---

## 🚀 Cómo ejecutar

1. Asegurarse de tener **Python 3.9+** y `numpy` instalado.
2. Si se dispone de un entorno virtual, activarlo:

   ```bash
   source .venv/bin/activate
   ```
3. Ejecutar el sistema principal:

   ```bash
   python main.py
   ```

   Esto generará:

   * 60 muestras simuladas (1 por segundo)
   * Bloques encadenados en `blockchain.json`
   * Un archivo `reporte.txt` con estadísticas y alertas.

---
