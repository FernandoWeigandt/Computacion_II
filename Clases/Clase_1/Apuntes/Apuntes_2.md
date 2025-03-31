# 🐍 Uso de getopt y argparse en Python

## 🎯 Fundamentos
Los argumentos de línea de comandos permiten a los programas recibir parámetros al ejecutarse desde la terminal. Python ofrece dos módulos principales para manejar estos argumentos:

- **getopt**: Manejo básico, similar a `getopt` en C.
- **argparse**: Más potente y flexible, recomendado para scripts más complejos.

## 🏛️ Uso de getopt
El módulo `getopt` permite manejar opciones de línea de comandos de manera similar a los scripts en shell.

🔹 **Ejemplo básico:**
```python
import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError:
        print("Uso: script.py -i <archivo_entrada> -o <archivo_salida>")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Uso: script.py -i <archivo_entrada> -o <archivo_salida>")
            sys.exit()
        elif opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-o", "--output"):
            output_file = arg
    
    print(f"Archivo de entrada: {input_file}, Archivo de salida: {output_file}")

if __name__ == "__main__":
    main(sys.argv[1:])
```

📌 **Ejecutar en la terminal:**
```bash
python script.py -i entrada.txt -o salida.txt
```

## 🚀 Uso de argparse
El módulo `argparse` es más robusto y permite definir argumentos de manera más estructurada.

🔹 **Ejemplo con argparse:**
```python
import argparse

parser = argparse.ArgumentParser(description="Ejemplo de argparse")
parser.add_argument("-i", "--input", required=True, help="Archivo de entrada")
parser.add_argument("-o", "--output", required=True, help="Archivo de salida")

args = parser.parse_args()
print(f"Archivo de entrada: {args.input}, Archivo de salida: {args.output}")
```

📌 **Ejecutar en la terminal:**
```bash
python script.py --input entrada.txt --output salida.txt
```


