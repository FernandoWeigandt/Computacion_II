# Sistema Concurrente de Análisis Biométrico con Blockchain Local

## 🧠 Descripción

Este sistema simula una prueba de esfuerzo biométrica, con procesamiento concurrente de señales y almacenamiento seguro en una cadena de bloques local.

### Componentes:
- **main.py**: genera señales, las analiza en paralelo y construye bloques validados.
- **verificar_cadena.py**: valida la integridad de la cadena y genera un reporte final.
- **blockchain.json**: archivo generado que contiene los bloques encadenados.
- **reporte.txt**: resumen final con estadísticas (incluye presión sistólica y diastólica) y alertas.

---

## 🚀 Cómo ejecutar

1. Asegurarse de tener Python 3.9+ y `numpy` instalado.
2. Activar el entorno virtual si existe:

```bash
source .venv/bin/activate
```

---

## ✅ Requisitos académicos cumplidos

- [x] Procesamiento concurrente de señales biométricas
- [x] Construcción y validación de cadena de bloques local
- [x] Generación de reporte final con estadísticas y alertas
- [x] Análisis de presión sistólica y diastólica por separados