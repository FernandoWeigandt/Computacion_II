1️⃣ Fundamentos de procesos
	•	Un proceso es una instancia de ejecución de un programa. Tiene atributos como el PID, el estado, y el espacio de direcciones.
	•	La diferencia principal entre un programa y un proceso es que un programa es un conjunto de instrucciones, mientras que un proceso es la ejecución de ese conjunto.

2️⃣ El modelo de procesos en UNIX/Linux
	•	Los procesos en UNIX/Linux tienen una jerarquía. El proceso padre puede crear un hijo usando fork().
	•	El primer proceso del sistema es init (o systemd), que se encarga de iniciar otros procesos y gestionar la terminación de procesos huérfanos.
	•	Herramientas como ps, top, pstree y htop nos permiten visualizar procesos activos en el sistema.

3️⃣ Manipulación de procesos con Python
	•	Usamos el módulo os para manipular procesos:
	•	fork(): Crea un nuevo proceso hijo.
	•	exec(): Reemplaza el proceso actual con otro programa.
	•	wait(): El padre espera a que el hijo termine, evitando que se quede como un proceso zombi.

4️⃣ Procesos zombis y huérfanos
	•	Un proceso zombi es un proceso que ha terminado pero no ha sido recogido por su proceso padre, lo que deja su entrada en la tabla de procesos.
	•	Un proceso huérfano es un proceso cuyo padre ha terminado antes que él, y es adoptado por el proceso init (PID 1).
	•	La mejor forma de evitar procesos zombis es asegurarse de que el padre llame a wait() para recoger el estado del hijo.

