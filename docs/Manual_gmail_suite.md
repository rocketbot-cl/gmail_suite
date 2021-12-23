



# Gmail G Suite
  
Módulo para realizar acciones en Gmail  
  
![banner](/docs/imgs/Banner_gmail_suite.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  



## Descripción de los comandos

### Configurar Servidor
  
Configurar Servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Credenciales||credentials.json|
|User||user@example.com|
|Sesión||session1|
|Asignar resultado a Variable||Variable|

### Enviar Email
  
Envia un email, previamente debe configurar el servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||session1|
|Para||to@mail.com, to2@mail.com|
|Copia||cc@mail.com, cc2@mail.com|
|Copia Oculta||bcc@mail.com, bcc2@mail.com|
|Asunto||Nuevo mail|
|Mensaje||Hi from Rocketbot!|
|Archivo Adjunto||C:\User\Desktop\test.txt|
|Carpeta (Varios archivos)||C:\User\Desktop\Files|

### Lista todos los email
  
Lista todos los email, se puede especificar un filtro
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro||subject:COMPRA|
|Label||INBOX|
|Sesión||session1|
|Ordenar por||{}|
|Asignar a variable||Variable|

### Lista emails no leídos
  
Lista emails no leídos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro||subject:COMPRA|
|Sesión||session1|
|Ordenar por||{}|
|Asignar a variable||Variable|

### Leer email por ID
  
Leer email por ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email||345|
|Sesión||session1|
|Asignar a variable||Variable|
|Ruta para descargar adjuntos||C:\User\Desktop|

### Crear Etiqueta
  
Crea una etiqueta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre Etiqueta||Ingrese nombre de la etiqueta|
|Sesión||session1|

### Mover email a etiqueta
  
Mueve email a una etiqueta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email||Ingrese ID del email|
|Nombre de la etiqueta||test|
|Sesión||session1|
|Asignar resultado a variable||Variable|

### Marcar email como no leído
  
Marcar email como no leído
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email||Ingrese ID del email|
|Sesión||session1|

### Cerrar Conexión
  
Cierra la conexión del servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||session1|

### Lista todas las etiquetas
  
Lista todas las etiquetas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||session1|
|Asignar a variable||Variable|

### Forward
  
Forward
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||session1|
|ID Mail||321|
|Para||to@mail.com, to2@mail.com|
|Copia||cc@mail.com, cc2@mail.com|
|Copia Oculta||bcc@mail.com, bcc2@mail.com|
|Asunto||Nuevo mail|

### Descargar adjuntos por ID
  
Descarga los archivos adjuntos de un correo y los guarda en una carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID del email a leer|345|
|Sesión|Sesión de Gmail|Default|
|Ruta para descargar adjuntos|Ruta donde se guardarán los adjuntos|C:/User/Desktop|
