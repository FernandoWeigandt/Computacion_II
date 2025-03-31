# Apuntes de la Primera Clase - Computación II

## 1️⃣ Configuración de Git
- **Git** es un sistema de control de versiones distribuido que permite rastrear cambios en archivos y colaborar sin sobrescribir el trabajo de otros.
- **Verificación e instalación:**
  - Se verificó la instalación con `git --version`.
  - Se instaló Git si era necesario.
- **Configuración de identidad:**
  - Se estableció el nombre y correo con `git config --global user.name` y `git config --global user.email`.
  - Se verificó la configuración con `git config --list`.

## 2️⃣ Creación del primer repositorio
- **Repositorio Git:** Es un espacio donde Git rastrea los cambios en un proyecto.
- **Diferencia entre repositorios locales y remotos:**
  - Local: en la máquina del usuario.
  - Remoto: alojado en servicios como GitHub o GitLab.
- **Comandos usados:**
  - `git init` para inicializar el repositorio.
  - `git status` para ver el estado de los archivos.
- **Directorio `.git`**: Contiene la información del repositorio y permite el seguimiento de versiones.

## 3️⃣ Estructura del repositorio del curso
- Se organizó el repositorio con la siguiente estructura:
  ```
  README.md
  /TP_1
  /TP_2
  /Clases
      /Clase_1
          /Apuntes
          /Ejercicios
          /Resumen_pedagogico
      ...
  /TRABAJO_FINAL
  ```
- Se creó un `README.md` con:
  - Información personal.
  - Expectativas sobre la materia.
  - Intereses en programación.
  - Hobbies.

## 4️⃣ Primer commit y flujo de trabajo Git
- **Ciclo de vida de los archivos:**
  1. **Working Directory** → Modificación de archivos.
  2. **Staging Area** → Archivos preparados para commit.
  3. **Repository** → Archivos confirmados en el historial.
- **Comandos usados:**
  - `git add` para añadir archivos al área de preparación.
  - `git commit -m "Mensaje"` para confirmar cambios.
  - `git log` para ver el historial de cambios.

## 5️⃣ Conexión con un repositorio remoto
- **Trabajo distribuido:** Permite trabajar en equipo y mantener copias seguras del código.
- **Comandos usados:**
  - `git remote add origin <URL>` para conectar con GitHub/GitLab.
  - `git push -u origin main` para subir los cambios.

## 6️⃣ Conceptos básicos de terminal Unix
- **Entrada/Salida en Unix/Linux:** Modelo que permite manipular datos de manera eficiente.
- **Tipos de E/S:**
  - `stdin` → Entrada estándar.
  - `stdout` → Salida estándar.
  - `stderr` → Errores estándar.
- **Redirección:**
  - `>` → Redirigir salida a un archivo.
  - `>>` → Añadir salida a un archivo existente.
  - `<` → Tomar entrada desde un archivo.
  - `2>` → Redirigir errores a un archivo.
  - `|` → Usar pipes para encadenar comandos.
- **Archivos especiales:** `/dev/null` para descartar salida.

## Estado actual
🎯 **Se completó la configuración del repositorio Git con la estructura requerida y los conceptos fundamentales.**

