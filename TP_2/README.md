
# TP2 — Sistema de Scraping y Análisis Web Distribuido

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
python3 server_processing.py -i 127.0.0.1 -p 8001
```

### 3) Levantar Servidor Asyncio (Parte A)
```bash
python3 server_scraping.py -i 127.0.0.1 -p 8000 --proc-host 127.0.0.1 --proc-port 8001
```

### 4) Probar con el 
```bash
python3 client.py https://www.google.com.ar 127.0.0.1 8000
```
Para ipv6
```bash
python3 server_processing.py -i "::1" -p 8001
python3 server_scraping.py -i "::1" -p 8000 --proc-host "::1" --proc-port 8001
python3 client.py https://www.google.com.ar
```

