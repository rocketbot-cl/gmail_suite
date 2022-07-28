# Gmail G Suite
  
Módulo para realizar acciones en Gmail  

*Read this in other languages: [English](Manual_gmail_suite.md), [Portugues](Manual_gmail_suite.pr.md), [Español](Manual_gmail_suite.es.md).*

*How to use: [English](/docs/how_to_use.md), [Portugues](/docs/how_to_use.pr.md), [Español](/docs/how_to_use.es.md).*
  
![banner](/docs/imgs/Banner_gmail_suite.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Configurar Servidor
  
Configurar el servidor del mail que se va a usar
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Credenciales|Ruta del archivo json descargado en el paso anterior|credentials.json|
|Usuario|Email que se usará para enviar correos. Puede estar en blanco si no enviarás emails.|user@example.com|
|Sesión|Nombre de la sesión que le vamos a asignar|session1|
|Asignar resultado a Variable|Resultado de la conexion|Variable|

### Enviar Email
  
Envia un email, previamente debe configurar el servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión que va a usar.|session1|
|Para|Destinatarios del mensaje. Deben estar separados por coma|to@mail.com, to2@mail.com|
|Copia|Destinatarios enviados por copia. Deben ir separados por coma|cc@mail.com, cc2@mail.com|
|Copia Oculta|Destinatarios enviados por copia oculta. Deben ir separado por coma|bcc@mail.com, bcc2@mail.comn|
|Asunto|Asunto del mensaje|Nuevo mail|
|Mensaje|Cuerpo del mail. Se pueden usar etiquetas html|Hi from Rocketbot!|
|Archivo Adjunto|Ruta del archivo que se desea adjuntar|C:\User\Desktop\test.txt|
|Carpeta (Varios archivos)|Ruta de la carpeta con los archivos que se desa adjuntar|C:\User\Desktop\Files|

### Lista todos los email
  
Lista todos los email, se puede especificar un filtro
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Puedes usar todas las opciones de filtro de gmail.|subject:ESCUELA|
|Carpeta|Carpeta desde donde se desa listar todos los emails|INBOX|
|Sesión|Nombre de la sesión que se va a usar|session1|
|Ordenar por|Ordena los correos listados por el parámetro deseado|New first|
|Asignar a variable|Nombre de la variable donde se guardará la lista de email|Variable|

### Lista emails no leídos
  
Lista emails no leídos, se puede especificar un filtro
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Puedes usar todas las opciones de filtro de gmail|subject:ESCUELA|
|Carpeta|Especificar nombre de la carpeta desde donde se quiere obtener los emails, por defecto inbox|inbox|
|Sesión|Nombre de la sesión que va a usar|session1|
|Ordenar por|Ordena los correos listados por el parámetro deseado|New first|
|Asignar a variable|Nombre de la variable donde se guardará la lista de email|Variable|

### Leer email por ID
  
Se puede especificar el ID de un email para leerlo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|Id obtenido en los comandos para listar email|345|
|Sesión|Nombre de la sesión que va a usar|session1|
|Asignar a variable|Nombre de la variable donde se guardará el contenido del mail leído|Variable|
|Ruta para descargar adjuntos|Ruta de la carpeta donde se guardarán los archivos adjuntos|C:\User\Desktop|

### Crear Etiqueta
  
Se puede crear una etiqueta con el nombre que desees
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre Etiqueta|Nombre de la etiqueta a crear|Ingrese nombre de la etiqueta|
|Sesión|Nombre de la sesión que va a usar|session1|

### Mover email a etiqueta
  
Mover email de una etiqueta a otra
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID obtenido en los comandos para listar email|345|
|Nombre de la etiqueta|Etiqueta a dónde se moverá el email|test|
|Sesión|Nombre de la sesión que va a usar|session1|
|Asignar resultado a variable|Variable donde se guardará. True si se movió el mail. Caso contrario, retomará False|Variable|

### Marcar email como no leído
  
Se puede marcar como no leido cualquier email previamente abierto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID obtenido en los comandos para listar email|Ingrese ID del email|
|Sesión|Nombre de la sesión que va a usar|session1|

### Lista todas las etiquetas
  
Obtiene una lista de todas las etiquetas del mail y las almacena en una variable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión que va a usar|session1|
|Listar todos los datos|Marca si deseas obtener todos los datos de las etiquetas tales como id, nombre, visibilidad, etc. Si no se marca, solo se obtendrá el id.|True|
|Asignar a variable|Variable donde se guardaran las etiquetas|Variable|

### Reenviar
  
Reenviar un email
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión que va a usar|session1|
|ID Mail|ID obtenido en los comandos para listar email|321|
|Para|Destinatarios del mensaje. Deben estar separados por coma|to@mail.com, to2@mail.com|
|Copia|Destinatarios enviados por copia. Deben estar separados por coma|cc@mail.com, cc2@mail.com|
|Copia Oculta|Destinatarios enviados por copia oculta. Deben estar separados por coma|bcc@mail.com, bcc2@mail.com|
|Asunto|Asunto del mensaje|Nuevo mail|

### Descargar adjuntos por ID
  
Descarga los archivos adjuntos de un correo y los guarda en una carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID del email a leer|345|
|Sesión|Sesión de Gmail|Default|
|Ruta para descargar adjuntos|Ruta donde se guardarán los adjuntos|C:/User/Desktop|

### Cerrar Conexión
  
Cierra la conexión del servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesión que va a usar|session1|
