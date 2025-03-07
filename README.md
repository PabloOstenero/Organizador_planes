# Organizador_planes

**¿Qué hace este programa?**

Este programa es un generador de horarios creado con la biblioteca Tkinter de Python. Permite al usuario ingresar una lista de tareas, la importancia y duración de cada tarea, y las horas libres disponibles cada día de la semana. Luego, el programa genera un horario que asigna las tareas a los espacios de tiempo disponibles, priorizando las tareas más importantes. El horario generado se muestra en una tabla dentro de la aplicación.

**Cómo usar el programa:**

El programa tiene tres pestañas principales: "Tareas", "Horas Libres" y "Horario Generado".

Pestaña "Tareas":

    Tarea: Ingrese el nombre de la tarea en el campo "Tarea".

    Importancia: Ingrese un número entero que represente la importancia de la tarea en el campo "Importancia". Los números más altos indican mayor importancia.

    Duración: Ingrese la duración estimada de la tarea en horas en el campo "Duración".

    Añadir Tarea: Haga clic en el botón "Añadir Tarea" para agregar la tarea a la lista de tareas. La tarea aparecerá en el Listbox debajo.

Repita los pasos anteriores para agregar todas sus tareas.

Pestaña "Horas Libres":

    Día: Seleccione el día de la semana en el menú desplegable "Día".

    Hora: Seleccione la hora libre disponible en el menú desplegable "Hora". Las horas se muestran en formato de 24 horas (8 a 19, correspondiendo a las 8:00 a.m. hasta las 7:00 p.m.).

    Añadir Hora: Haga clic en el botón "Añadir Hora" para agregar la hora libre al día seleccionado.

Repita los pasos anteriores para agregar todas sus horas libres disponibles en cada día.

Pestaña "Horario Generado":

    Generar Horario: Una vez que haya agregado todas sus tareas y horas libres, haga clic en el botón "Generar Horario".

    El programa generará un horario basado en sus entradas y lo mostrará en formato de tabla en el widget de texto debajo del botón. La tabla mostrará las tareas asignadas para cada hora de cada día.

Consideraciones Importantes:

El programa prioriza las tareas con mayor importancia.

Las tareas se asignan secuencialmente a las horas libres disponibles.

Asegúrese de ingresar números enteros válidos para la importancia y la duración de las tareas.

Si una tarea no puede completarse en un solo día, el programa la continuará asignando en días posteriores, siempre y cuando haya horas libres disponibles.

El horario se genera en función del orden en que ingresó las tareas y las horas libres, junto con su importancia y duración.

Este programa es una herramienta útil para organizar su tiempo y asegurarse de que las tareas más importantes se completen.

