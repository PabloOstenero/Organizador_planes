# archivo_preguntas.md

## Ciclo de vida del dato (5b):

**¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?**

Actualmente, el ciclo de vida de los datos es muy corto. Los datos (tareas y horas libres) se generan cuando el usuario los introduce a través de la interfaz gráfica de usuario (GUI). Se almacenan en memoria (en los diccionarios `self.tareas` y `self.horas_libres`). Los datos persisten solo durante la ejecución de la aplicación. Cuando la aplicación se cierra, los datos se pierden. No hay almacenamiento persistente ni mecanismo de eliminación.

**¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?**

La estrategia para la integridad de los datos es básica. Se realiza la validación de datos cuando el usuario introduce información de la tarea (verificando que la importancia y la duración sean números). Sin embargo, no existen mecanismos para evitar inconsistencias como tareas superpuestas o reservas dobles de espacios de tiempo.

**Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?**

Para gestionar los datos de manera eficiente, agregaría:

1.  **Almacenamiento persistente:** Usar un archivo local (por ejemplo, JSON, CSV) o una base de datos ligera (por ejemplo, SQLite) para almacenar las tareas y las horas libres. Esto permitiría a los usuarios guardar y cargar sus horarios.
2.  **Validación de datos:** Implementar una validación más robusta. Esto incluiría la comprobación de:
    *   Espacios de tiempo superpuestos dentro de un día.
    *   Tareas conflictivas.
    *   Duración negativa o cero.
3.  **Serialización/Deserialización de datos:** Utilizar una biblioteca como `json` o `pickle` para serializar las estructuras de datos en un formato que pueda almacenarse en un archivo y deserializarlo al cargar.
4.  **Modelo de datos:** Definir una clase para "Tarea" que encapsule las propiedades de la tarea (nombre, importancia, duración) y proporcione métodos para la validación.

## Almacenamiento en la nube (5f):

**Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?**

El software no utiliza actualmente el almacenamiento en la nube. Si tuviera que integrarlo, lo haría de la siguiente manera:

*   **Autenticación y autorización:** Utilizar un mecanismo de autenticación seguro (por ejemplo, OAuth 2.0) para autenticar a los usuarios y controlar el acceso a sus datos.
*   **Cifrado:** Cifrar los datos tanto en tránsito (HTTPS) como en reposo (utilizando los servicios de cifrado del proveedor de la nube o una biblioteca de cifrado de terceros).
*   **Copia de seguridad de datos y redundancia:** Aprovechar las funciones de copia de seguridad y redundancia del proveedor de la nube para garantizar una alta disponibilidad y evitar la pérdida de datos.
*   **Control de acceso:** Implementar políticas estrictas de control de acceso para limitar quién puede acceder a los datos.

**¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?**

Actualmente, no se consideran alternativas de almacenamiento de datos porque la aplicación solo utiliza el almacenamiento en memoria. Si se agregara almacenamiento persistente, las opciones serían:

*   **Almacenamiento de archivos local (JSON, CSV, SQLite):** Fácil de implementar para una aplicación de un solo usuario. SQLite es una buena opción porque es una base de datos autocontenida que no requiere un servidor separado.
*   **Base de datos basada en la nube (por ejemplo, Google Cloud Firestore, AWS DynamoDB):** Adecuada para escenarios multiusuario donde los datos deben sincronizarse entre dispositivos y usuarios.
*   **Almacenamiento en la nube (por ejemplo, AWS S3, Google Cloud Storage):** Útil para almacenar archivos grandes o copias de seguridad de los datos.

La "solución" actual (o la falta de ella) probablemente se eligió por la simplicidad en el desarrollo inicial.

**Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?**

Para integrar el almacenamiento en la nube:

1.  **Elegir un proveedor de nube y un servicio:** Seleccionar un proveedor de nube (AWS, Google Cloud, Azure) y un servicio de almacenamiento (por ejemplo, almacenamiento de objetos como S3 o una base de datos NoSQL como DynamoDB).
2.  **Implementar la autenticación:** Integrar un mecanismo de autenticación seguro (por ejemplo, utilizando el SDK del proveedor de la nube) para permitir a los usuarios iniciar sesión y acceder a sus datos.
3.  **Desarrollar lógica de sincronización de datos:** Crear lógica para sincronizar datos entre la aplicación local y el almacenamiento en la nube. Esto implicaría cargar los cambios locales en la nube y descargar las actualizaciones de la nube.
4.  **Manejar errores de red:** Implementar el manejo de errores para gestionar con elegancia los problemas de conectividad de red y los conflictos de sincronización de datos.

## Seguridad y regulación (5i):

**¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?**

Actualmente, la aplicación no tiene prácticamente ninguna medida de seguridad implementada. Los datos se almacenan en la memoria y no están protegidos contra el acceso o la modificación no autorizados.

**¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?**

Dado que la aplicación no almacena ni transmite datos personales, el GDPR y regulaciones similares no serían directamente aplicables *en su estado actual*. Sin embargo, si la aplicación se modificara para:

*   Almacenar cuentas de usuario y perfiles.
*   Compartir horarios con otros usuarios.
*   Recopilar cualquier información personal (incluso nombres),

Entonces el GDPR se aplicaría. Necesitaría:

*   Obtener el consentimiento del usuario para la recopilación de datos.
*   Proporcionar a los usuarios la capacidad de acceder, modificar y eliminar sus datos.
*   Implementar técnicas de anonimización o seudonimización de datos.
*   Garantizar la seguridad de los datos mediante el cifrado y los controles de acceso.

**Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?**

Los principales riesgos son:

*   Pérdida de datos: Si la aplicación falla, se perderán todos los datos no guardados.
*   Acceso no autorizado: Si alguien obtiene acceso al ordenador donde se está ejecutando la aplicación, podría potencialmente ver o modificar los datos.
*   Corrupción de datos: Los errores en el código podrían conducir potencialmente a la corrupción de los datos.

Para abordar estos riesgos:

*   Implementar el almacenamiento persistente con copias de seguridad regulares.
*   Utilizar el cifrado para proteger los datos en reposo.
*   Implementar una validación de entrada adecuada para evitar la corrupción de los datos.

## Implicación de las THD en negocio y planta (2e):

**¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?**

En su forma actual, el impacto del software en un entorno empresarial o industrial sería limitado. Sin embargo, una versión más sofisticada podría tener los siguientes impactos:

*   Mejora de la programación de recursos: Ayudar a los gerentes a programar empleados, equipos o recursos de manera más eficiente.
*   Flujo de trabajo optimizado: Asegurarse de que las tareas se completen de manera oportuna, reduciendo los cuellos de botella y mejorando la productividad general.
*   Mejor gestión de proyectos: Facilitar la planificación de proyectos y la asignación de tareas, ayudando a los equipos a mantenerse en el camino correcto y cumplir con los plazos.

**¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?**

Una versión refinada podría:

*   Proporcionar a los gerentes visibilidad en tiempo real de la asignación de recursos.
*   Generar informes sobre las tasas de finalización de tareas y la utilización de recursos.
*   Ayudar a identificar áreas donde se pueden mejorar los procesos.
*   Apoyar la toma de decisiones basada en datos proporcionando información sobre la distribución de la carga de trabajo y las necesidades de recursos.

**Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?**

Otros entornos que podrían beneficiarse incluyen:

*   Educación: Los estudiantes podrían usarlo para gestionar sus horarios de estudio.
*   Sanidad: Los médicos o enfermeras podrían usarlo para programar citas o gestionar las tareas de atención al paciente.
*   Uso personal: Los individuos podrían usarlo para planificar sus actividades diarias o semanales.

## Mejoras en IT y OT (2f):

**¿Cómo puede tu software facilitar la integración entre entornos IT y OT?**

Para integrar IT y OT, el software podría:

*   Recopilar datos de sistemas OT: Conectarse a sensores, PLCs u otros dispositivos OT para recopilar datos en tiempo real sobre el estado del equipo, las tasas de producción o las condiciones ambientales.
*   Usar APIs: Exponer APIs REST para permitir que los sistemas IT (por ejemplo, ERP, MES) accedan a los datos de programación e integrarlos en sus flujos de trabajo.
*   Proporcionar una vista unificada: Mostrar los datos OT junto con los horarios de las tareas, dando a los operadores una visión completa del proceso de producción.
*   Permitir la monitorización y el control remotos: Permitir a los usuarios autorizados monitorizar y controlar de forma remota los dispositivos OT en función de los datos de programación.

**¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?**

Los procesos específicos que podrían beneficiarse incluyen:

*   Programación de la producción: Ajustar automáticamente los horarios de producción en función del estado del equipo en tiempo real y las previsiones de la demanda.
*   Gestión del mantenimiento: Programar las tareas de mantenimiento en función de los patrones de uso del equipo y las tasas de fallo predichas.
*   Gestión de inventario: Optimizar los niveles de inventario coordinando los horarios de producción con los datos de inventario.

**Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?**

Para mejorar los procesos tecnológicos:

*   Conectarse a las APIs de calendario (Google Calendar, Outlook Calendar) para rellenar automáticamente las horas libres.
*   Integrarse con herramientas de gestión de tareas (por ejemplo, Todoist, Trello) para importar tareas y seguir el progreso.
*   Utilizar el aprendizaje automático para predecir la duración de las tareas y optimizar los horarios.

## Tecnologías Habilitadoras Digitales (2g):

**¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?**

Actualmente, el proyecto utiliza tecnología GUI básica (Tkinter). Estas son las THD que *podrían* integrarse:

*   Cloud Computing: Para el almacenamiento de datos, la sincronización y la escalabilidad (como se ha comentado anteriormente).
*   Internet de las Cosas (IoT): Para recopilar datos en tiempo real de sensores y dispositivos.
*   Análisis de Big Data: Para analizar los datos de programación e identificar patrones o tendencias.
*   Inteligencia Artificial (IA) / Aprendizaje Automático (ML): Para predecir la duración de las tareas, optimizar los horarios y automatizar la toma de decisiones.
*   Informática móvil: Para desarrollar una aplicación móvil que permita a los usuarios acceder a sus horarios sobre la marcha.

**¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?**

Estas tecnologías:

*   Permitirían la toma de decisiones basada en datos.
*   Automatizarían las tareas y mejorarían la eficiencia.
*   Extenderían el alcance del software a nuevos dispositivos y usuarios.
*   Proporcionarían información en tiempo real sobre la asignación de recursos y el progreso de las tareas.

**Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?**

Para implementar las THD:

1.  Comenzar con una arquitectura basada en la nube: Migrar el almacenamiento y el procesamiento de datos a la nube.
2.  Desarrollar APIs para el acceso a los datos: Crear APIs para permitir que otros sistemas accedan e integren los datos de programación.
3.  Integrar el aprendizaje automático para la optimización: Utilizar ML para predecir la duración de las tareas y optimizar los horarios.
4.  Desarrollar una aplicación móvil: Crear una aplicación móvil para proporcionar a los usuarios un acceso conveniente a sus horarios.
5.  Implementar la conectividad IoT: Conectarse a sensores y dispositivos para recopilar datos en tiempo real.
