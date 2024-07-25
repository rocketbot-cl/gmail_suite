



# Gmail G Suite
  
Conéctese a través de la API de Google a su cuenta de Gmail, lea, envíe y administre su bandeja de entrada, etiquetas y carpetas de correo electrónico.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Configurar Servidor  
Configurar el servidor del mail que se va a usar

2. Enviar Email  
Envia un email, previamente debe configurar el servidor

3. Lista todos los email  
Lista todos los email, se puede especificar un filtro

4. Lista emails no leídos  
Lista emails no leídos, se puede especificar un filtro

5. Leer email por ID  
Se puede especificar el ID de un email para leerlo

6. Obtener hilo por ID  
Obtener el hilo completo de un correo electrónico por ID

7. Crear Etiqueta  
Se puede crear una etiqueta con el nombre que desees

8. Mover email a etiqueta  
Mover email de una etiqueta a otra

9. Marcar email como no leído  
Se puede marcar como no leido cualquier email previamente abierto

10. Lista todas las etiquetas  
Obtiene una lista de todas las etiquetas del mail y las almacena en una variable

11. Reenviar  
Reenviar un email

12. Responder email  
Este comando permite responder un email por su ID

13. Descargar adjuntos por ID  
Descarga los archivos adjuntos de un correo y los guarda en una carpeta

14. Cerrar Conexión  
Cierra la conexión del servidor  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**mail-parser**](https://pypi.org/project/mail-parser/)- [**google-api-python-client**](https://pypi.org/project/google-api-python-client/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)