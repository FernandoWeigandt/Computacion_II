
# TP2 — Sistema de Scraping y Análisis Web Distribuido (Starter)

Starter mínimo funcional (Parte A y B) con comunicación binaria (longitud + JSON) y estructura modular.

## Quickstart

### 1) Crear venv e instalar deps
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Levantar Servidor de Procesamiento (Parte B)
En otra terminal:
```bash
python server_processing.py -i :: -p 9000 -n 0
```

### 3) Levantar Servidor Asyncio (Parte A)
```bash
python server_scraping.py -i :: -p 8000 -w 4 --proc-host :: --proc-port 9000
```

### 4) Probar con el cliente
```bash
python client.py https://example.com
```
