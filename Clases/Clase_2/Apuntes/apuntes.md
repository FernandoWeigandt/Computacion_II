# 📌 Procesos en Sistemas Operativos

## 🔹 Fundamentos de procesos
Un **proceso** es una instancia en ejecución de un programa. Cada proceso posee un identificador único (**PID**), un estado (**nuevo, listo, en ejecución, bloqueado o terminado**) y una estructura en la memoria que incluye código, datos y pila. 

🔹 **Diferencia entre programa y proceso:** Un programa es un conjunto de instrucciones almacenadas en disco, mientras que un proceso está activo y gestionado por el sistema operativo.

⚙️ Los sistemas operativos modernos utilizan **multiprogramación**, donde múltiples procesos comparten recursos de manera eficiente.

## 🏛️ El modelo de procesos en UNIX/Linux
En **UNIX/Linux**, los procesos forman una **jerarquía**, donde cada proceso padre puede crear procesos hijos mediante la llamada `fork()`.

🔹 **Proceso inicial:** El primer proceso en el sistema es `init` o `systemd`, que inicia y supervisa todos los demás procesos. 

🔍 **Herramientas útiles:**
```bash
ps aux       # Muestra la lista de procesos en ejecución
pstree       # Muestra la jerarquía de procesos en forma de árbol
htop         # Interfaz interactiva para monitorear procesos
```

## 🐍 Manipulación de procesos con Python
Python permite la creación y manipulación de procesos mediante el módulo `os`:

- 🛠️ Crear un proceso hijo:
```python
import os

pid = os.fork()
if pid == 0:
    print("Soy el proceso hijo", os.getpid())
else:
    print("Soy el proceso padre", os.getpid())
```

- 🔄 Reemplazar un proceso con `exec()`:
```python
import os

os.execlp("ls", "ls", "-l")  # Reemplaza el proceso actual con el comando 'ls -l'
```

- ⏳ Esperar a que un proceso hijo termine:
```python
import os

pid = os.fork()
if pid == 0:
    print("Hijo ejecutando...")
else:
    os.wait()
    print("Hijo terminado, padre sigue ejecutando")
```

## 💀 Procesos zombis y huérfanos
- 🧟 **Proceso zombi:** Ha terminado su ejecución, pero su entrada en la tabla de procesos aún no ha sido eliminada por su proceso padre. Ocurre cuando el padre no llama a `wait()`.

- 👤 **Proceso huérfano:** Su padre ha terminado antes que él. En sistemas UNIX, son adoptados por `init/systemd`, asegurando su correcta gestión.

🕵️ **Detección de procesos zombis:**
```bash
ps aux | grep Z
```

✂️ **Eliminación:**
```bash
kill -9 <PID_DEL_PADRE>
```

## 🏋️ Ejercicios prácticos
1. 📜 Crear un proceso hijo en Python y hacer que ambos impriman mensajes.
2. 🔁 Implementar un programa que genere múltiples procesos usando `fork()`.
3. ⚠️ Simular un proceso zombi y mostrar cómo eliminarlo.
4. 🖥️ Implementar un **servidor multiproceso** que atienda múltiples clientes simultáneamente.

## 🎯 Conclusión
El manejo de procesos es fundamental en sistemas operativos. Permite la ejecución concurrente de tareas, mejorando la eficiencia de los recursos del sistema. 

🚀 Con **Python**, es posible crear y gestionar procesos de manera sencilla, facilitando la implementación de aplicaciones que requieran ejecución paralela.


