# Guía sobre getopt y argparse en Python

## 1️⃣ Objetivos de Aprendizaje
Al finalizar esta sesión, deberías ser capaz de:

- Entender la importancia de manejar argumentos de línea de comandos en scripts de Python.
- Utilizar `getopt` para parsear argumentos simples.
- Implementar `argparse` para manejar argumentos de manera más robusta y flexible.
- Crear un script funcional que acepte y procese argumentos desde la terminal.

## 2️⃣ Activación de Conocimientos Previos
Antes de comenzar:

- ¿Qué sabes sobre los argumentos de línea de comandos?
- ¿Has usado alguna vez la terminal para ejecutar scripts?
- Relación con conceptos previos: ejecución de programas e interacción con el sistema operativo.

## 3️⃣ Explicación Teórica
- **Argumentos de línea de comandos**: permiten pasar información a un script al momento de su ejecución.
- **Diferencia entre `getopt` y `argparse`**:
  - `getopt`: útil para argumentos simples, basado en la sintaxis de Unix.
  - `argparse`: más flexible, permite argumentos posicionales y opciones avanzadas.
- **Importancia**: Facilita la personalización y reutilización de scripts en diferentes escenarios.

## 4️⃣ Demostración Práctica
### Uso de `getopt`
Ejemplo básico:
```python
import sys
import getopt

def main(argv):
    input_file = ""
    output_file = ""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('script.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('script.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    print(f'Archivo de entrada: {input_file}')
    print(f'Archivo de salida: {output_file}')

if __name__ == "__main__":
    main(sys.argv[1:])
```

### Uso de `argparse`
Ejemplo avanzado:
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Ejemplo de argparse")
    parser.add_argument("input", help="Archivo de entrada")
    parser.add_argument("output", help="Archivo de salida")
    parser.add_argument("-v", "--verbose", action="store_true", help="Activar modo detallado")
    args = parser.parse_args()

    print(f'Archivo de entrada: {args.input}')
    print(f'Archivo de salida: {args.output}')
    if args.verbose:
        print("Modo detallado activado")

if __name__ == "__main__":
    main()
```

## 5️⃣ Desafío Práctico
Crea un script en Python que:
- Use `argparse` para aceptar un archivo de entrada y otro de salida.
- Opcionalmente, incluya un argumento para definir un formato de salida (`--format`).

## 6️⃣ Punto de Control
- ¿Cuál es la diferencia entre `getopt` y `argparse`?
- ¿Cómo harías que un argumento sea obligatorio en `argparse`?
- ¿Qué ventajas tiene `argparse` sobre `getopt`?

## 7️⃣ Extensión y Profundización
- Manejo de tipos de datos con `argparse` (enteros, listas, booleanos).
- Mención de temas futuros como programación concurrente y APIs.

## 8️⃣ Síntesis y Cierre
- Resumen de conceptos clave.
- Recursos adicionales:
  - Documentación oficial de [`argparse`](https://docs.python.org/3/library/argparse.html).
  - Tutoriales recomendados.

## 9️⃣ Recordatorios
- **Comparte avances con el profesor y compañeros**.
- **No avances demasiado rápido sin entender los fundamentos**.
- **Consulta la documentación si tienes dudas adicionales**.

