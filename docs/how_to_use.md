# Como usar este modulo
Para trabajar con este modulo es necesario activar la API de gmail. Para esto, debes seguir los siguientes pasos.
* Ir a [Consola de Google](https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard%3Fproject%3Dprueba-312216%26hl%3Des&folder=&organizationId=777182023349&hl=es) para crear un nuevo proyecto (Si ya tienes uno creado, omita este paso) y complete los datos indicados en el formulario

![](imgs/proyectonuevo.png)

En la barra superior verás el nombre del proyecto. Si no se visualiza, cambie al proyecto creado haciendo click en la en el menu que se encuentra remarcado en la imagen.

![](imgs/seleccionarproyecto.png)

Si tienes el mensaje "No cuentas con los permisos suficientes para ver esta página." como se muestra en la imagen anterior, de click en **API y Servicios** del panel izquierdo, y luego de cambiar a la página, hacer click en **HABILITAR API Y SERVICIOS**

![](imgs/habilitarapiyservicios.png)

Dentro del buscador "Buscar API y servicios" escriba **Gmail API**. Luego, habilitar la API dando click en **Habilitar**

![](imgs/gamialapi.png)

Tardará un momento en cargar y la página redireccionará a la página de configuración de la API.

* Haga click en **CREAR CREDENCIALES**, para crear las credenciales

![](imgs/crearcredenciales.png)

El primer paso es seleccionar el tipo de credencial. Seleccionamos **Gmail API** y tildamos la opción **Datos del usuario**. A continuación haga click en siguiente.

![](imgs/tipocredencial.png)

En la pantalla de consentimiento, escribir un nombre para la aplicación y seleccionar un correo electrónico.

![](imgs/pantallaconsentimiento.png)

En la pantalla de permisos, haga click en **AGREGAR O QUITAR PERMISOS**. Se abrirá un modal para seleccionar los permisos. En el filtro escriba **Gmail API**, click en el menu desplegable **Filas por pagina** y seleccione **100** para poder ver todas las opciones, seleccione todas tildando **API**, luego click en **Actualizar**.


![](imgs/agregarpermisos.png)

![](imgs/actualizar.png)

Una vez se agreguen los permisos seleccionados, da click en **GUARDAR Y CONTINUAR**

![](imgs/guardarycontinuar.png)

Finalmente, en la pantalla de OAuth, seleccionar el tipo de aplicación **APP de escritorio**, y agregar un nombre. Finalizamos dando click en crear.

![](imgs/oauth.png)

Nos creará las credenciales, damos click en descargar y luego en listo. Es importante mantener el archivo descargado. Se utilizará más adelante en el módulo.

![](imgs/descargar.png)

En el menú de la izquierda, al dar click en **Pantalla de consentimiento**, si tienes una cuenta corporativa de gmail, podrás utilizar la API indefinidamente y verás que el tipo de usuario es **Interno**. Si cuentas con una cuenta gmail gratuita, tendrás que dar el consentimiento una vez a la semana para poder conectarte a tu cuenta de correo y verás que tu tipo de usuario es **Externo** y deberás agregar usuarios de prueba.

![](imgs/interno.png)

![](imgs/externo.png)

Para prevenir confirmar cada semana, puedes publicar la aplicación para que google la apruebe y puedas usarla indefinidamente.

---

# How to use
## Obtaining credentials:
To work with this module it is necessary to activate the gmail API. For this, you must follow the following steps.
* Go to [Google console](https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard%3Fproject%3Dprueba-312216%26hl%3Des&folder=&organizationId=777182023349&hl=es) to create a new project (If you already have one created, skip this step) and complete the information indicated in the form

![](imgs/proyectonuevo.png)

In the top bar you will see the name of the project. If it is not displayed, change to the created project by clicking on the in the menu that is highlighted in the image.

![](imgs/seleccionarproyecto.png)

If you get the message "You do not have sufficient permissions to view this page." As shown in the image above, click on **API and Services** on the left panel, and after switching to the page, click on **ENABLE API AND SERVICES**

![](imgs/habilitarapiyservicios.png)

Within the browser "Search APIs and services" type **Gmail API**. Then, enable the API by clicking on **Enable**

![](imgs/gamialapi.png)

It will take a moment to load and the page will redirect to the API settings page.

* Click on **CREATE CREDENTIALS**, to create the credentials

![](imgs/crearcredenciales.png)

The first step is to select the type of credential. We select **Gmail API** and check the option **User data**. Then click next.

![](imgs/tipocredencial.png)

On the consent screen, type a name for the app and select an email.

![](imgs/pantallaconsentimiento.png)

On the permissions screen, click **ADD OR REMOVE PERMISSIONS**. A modal will open to select the permissions. In the filter type **Gmail API**, click on the dropdown menu **Rows per page** and select **100** to see all the options, select all by checking **API**, then click on * *Update**

![](imgs/agregarpermisos.png)

![](imgs/actualizar.png)

Once the selected permissions are added, click on **SAVE AND CONTINUE**

![](imgs/guardarycontinuar.png)

Finally, on the OAuth screen, select the application type **Desktop APP**, and add a name. We finish by clicking on create.

![](imgs/oauth.png)

It will create the credentials for us, we click on download and then on ready. It is important to keep the file downloaded. It will be used later in the module.

![](imgs/descargar.png)

In the menu on the left, when you click on **Consent screen**, if you have a corporate gmail account, you will be able to use the API indefinitely and you will see that the type of user is **Internal**. If you have a free gmail account, you will have to give consent once a week to be able to connect to your email account and you will see that your user type is **External** and you will have to add test users.

![](imgs/interno.png)

![](imgs/externo.png)

To prevent committing every week, you can publish the app for google approval and you can use it indefinitely.


---