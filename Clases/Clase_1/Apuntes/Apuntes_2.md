Resumen de lo aprendido:

1. Conceptos clave sobre getopt y argparse:
	•	Argumentos de línea de comandos: Son fundamentales para hacer que nuestros scripts sean más dinámicos y reutilizables, permitiendo que el usuario pase datos directamente desde la terminal.
	•	Uso de getopt: Aprendimos que es una opción más sencilla y menos robusta que argparse, adecuada para scripts simples. getopt permite procesar argumentos de línea de comandos pero no proporciona muchas opciones para validaciones o personalización.
	•	Uso de argparse: argparse es mucho más potente, permitiendo la validación de entradas, el uso de opciones predeterminadas, la validación de tipos de datos y la creación de una interfaz de usuario más amigable. Además, maneja opciones complejas como argumentos obligatorios y ayuda contextual.

2. Aplicaciones prácticas con argparse:
	•	Definición de argumentos: Aprendimos cómo definir y usar argumentos de línea de comandos, y cómo darles un valor por defecto.
	•	Validaciones y restricciones: Implementamos validaciones para asegurarnos de que los datos proporcionados sean correctos (como la validación de números en un rango).
	•	Manejo de listas de valores: Trabajamos con la opción de permitir múltiples valores para un argumento usando argparse.
	•	Mensajes de ayuda: Usamos la funcionalidad de argparse para generar mensajes de ayuda automáticos para los usuarios que ejecuten el script con la opción -h o --help.

3. Diferencias entre getopt y argparse:
	•	getopt: Menos flexible, pero rápido y adecuado para scripts sencillos con pocos argumentos. No permite mucha validación de datos.
	•	argparse: Más robusto y flexible, ideal para scripts más complejos que requieren validación, argumentos obligatorios, mensajes de ayuda, y tipos de datos específicos.

4. Ejercicios realizados:
	•	Creación de un script funcional: Aprendimos cómo crear un script que reciba y procese argumentos como la edad, nombre, hobbie y otros, y cómo manipular esos datos dentro del programa.
	•	Eliminación de archivos específicos: Aprendimos a usar la terminal para eliminar archivos .gitkeep en toda una carpeta y subcarpetas con un solo comando.

5. Feedback y desempeño:
	•	Compromiso con los conceptos: Mostraste un buen nivel de comprensión y aplicación de los conceptos, reflexionando sobre las diferencias entre getopt y argparse.
	•	Resolución de errores: Fuiste capaz de corregir los errores en tu código cuando se presentaron, y aprendiste a identificar las posibles soluciones.
	•	Evolución en el uso de herramientas: Con argparse, mostraste un buen dominio en el uso de la terminal para crear scripts funcionales y bien estructurados.

Áreas de mejora:
	•	Mayor práctica con validaciones: Aunque entendiste cómo manejar los argumentos, seguir practicando las validaciones y los tipos de datos será útil para abordar scripts más complejos.
	•	Exploración de funcionalidades avanzadas: Continuar aprendiendo sobre características más avanzadas de argparse, como subcomandos o configuraciones personalizadas, será beneficioso.
