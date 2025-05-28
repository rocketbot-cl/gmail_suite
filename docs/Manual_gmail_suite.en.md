



# Gmail G Suite
  
Connect through Google API to your Gmail account, read, send and manage your email inbox, labels and folders.  

*Read this in other languages: [English](Manual_gmail_suite.md), [Português](Manual_gmail_suite.pr.md), [Español](Manual_gmail_suite.es.md)*
  
![banner](imgs/Banner_gmail_suite.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

# How to use

*Read this in other languages: [English](how_to_use.md), [Portugues](how_to_use.pr.md), [Español](how_to_use.es.md).*

## Obtaining credentials:
To work with this module it is necessary to activate the gmail API. For this, you must follow the following steps.
* Go to [Google console](https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard%3Fproject%3Dprueba-312216%26hl%3Des&folder=&organizationId=777182023349&hl=es) to create a new project (If you already have one created, skip this step) and complete the information indicated in the form

![](imgs/proyectonuevo.png)

In the top bar you will see the name of the project. If it is not displayed, change to the created project by clicking on the in the menu that is highlighted in the image.

![](imgs/seleccionarproyecto.png)

If you get the message "You do not have sufficient permissions to view this page." As shown in the image above, click on **API and Services** on the left panel, and after 
switching to the page, click on **ENABLE API AND SERVICES**

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

To prevent committing every week, you can 
publish the app for google approval and you can use it indefinitely.
## Description of the commands

### Server Configuration
  
Configure the mail server to be used
|Parameters|Description|example|
| --- | --- | --- |
|Credentials|Path of the json file donwloaded in the previus step |credentials.json|
|Port (Optional)||8080|
|User|Email that will be used to send emails. It can be blank if you will not send emails|user@example.com|
|Session|Name of the sesion we are going to asign|session1|
|Assign result to a Variable|Result of the connection|Variable|

### Send Email
  
Send email, before you must configurate the server
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session we will be use|session1|
|To|Message receivers. They must be separated by commas|to@mail.com, to2@mail.com|
|Cc|Receivers sent by copy. They must be separated by commas|cc@mail.com, cc2@mail.com|
|Bcc|Receivers sent by copy hidden. They must be separated by commas|bcc@mail.com, bcc2@mail.com|
|Subject|Message subject|New mail|
|Body|Body of the message. Can be use html labels|Hi from Rocketbot!|
|Attached File|Path of the file that we want to attach|C:\User\Desktop\test.txt|
|Folder (Multiple files)|Path of the folder with the files we want to attach|C:\User\Desktop\Files|
|Assign result to a Variable|Result of the connection|Variable|

### List all email
  
List all email, you can specify a filter
|Parameters|Description|example|
| --- | --- | --- |
|Filter|You can use all options of filters from gmail|subject:SCHOOL|
|Number of emails to retrieve|Number of emails to retrieve, default 100, maximum 500.|500|
|Folder|Folder where all emails are listed|INBOX|
|Order by|Sort the listed emails by the desired parameter|New first|
|Thread ID|Check to get message thread id|True|
|Session|Name of session will be used|session1|
|Asign to var|Name of the variable where the email list will be saved|Variable|

### List unread emails
  
List unread emails, you can specify a filter
|Parameters|Description|example|
| --- | --- | --- |
|Filter|You can use all gmail filter options|subject:SCHOOL|
|Folder|Specify the name of the folder from where you want to get the emails, by default inbox|inbox|
|Session|Name of the session to use|session1|
|Order by|Sort the listed emails by the desired parameter|New first|
|Asign to var|Name of the variable where the email list will be saved|Variable|

### Read email for ID
  
You can specify the ID of an email to read it
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Id obtained in the commands to list email|345|
|Session|Name of the session to use|session1|
|Asign to var|Name of the variable where the content of the read mail will be saved|Variable|
|Path for download attachment|Path of the folder where the attachments will be saved|C:\User\Desktop|

### Get thread by ID
  
Get the whole thread of an email by ID
|Parameters|Description|example|
| --- | --- | --- |
|Thread ID|Id obtained in the commands to list email|345|
|Format|Format of the returned data|Full|
|Session|Name of the session to use|session1|
|Asign to var|Name of the variable where the content of the read mail will be saved|Variable|

### Create Label
  
You can create a label with the name you want
|Parameters|Description|example|
| --- | --- | --- |
|Label Name|Name of the tag to create|Enter the name of the tag|
|Session|Name of the session to use|session1|

### Move email to label
  
Move email from one label to another
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|ID obtained in the commands to list email|345|
|Label Name|Label where the email will be moved to|new|
|Label Name to remove|Label to remove from email (Optional)|old|
|Session|Name of the session to use|session1|
|Asign result to var|Variable where it will be saved. True if the mail was moved. Otherwise, it will return False|Variable|

### Mark email as unread
  
Any previously opened email can be marked as unread
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|ID obtained in the commands to list email|Enter Email ID|
|Session|Name of the session to use|session1|

### List all labels
  
Get a list of all mail labels and store them in a variable
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session to use|session1|
|List all data|Check if you want to get all the tag data such as id, name, visibility, etc. If it is not checked, only the id will be obtained.|True|
|Asign to var|Variable where the labels will be saved|Variable|

### Forward
  
Forward an email
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session to use|session1|
|ID Mail|ID obtained in the commands to list email|321|
|To|Message receivers. They must be separated by commas|to@mail.com, to2@mail.com|
|Cc|Recipients sent by copy. They must be separated by commas|cc@mail.com, cc2@mail.com|
|Bcc|Recipients sent by hiden copy. They must be separated by commas|bcc@mail.com, bcc2@mail.com|
|Subject|Message subject|New email|

### Reply email
  
This command allows you to reply to an email by its ID
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session to use|session1|
|ID Mail|ID obtained in the commands to list email|321|
|To|Message receivers. They must be separated by commas|to@mail.com, to2@mail.com|
|Cc|Recipients sent by copy. They must be separated by commas|cc@mail.com, cc2@mail.com|
|Bcc|Recipients sent by hiden copy. They must be separated by commas|bcc@mail.com, bcc2@mail.com|
|Subject|Message subject|New email|

### Download attachments for ID
  
Downloads email attachments and saves them in a folder
|Parameters|Description|example|
| --- | --- | --- |
|Email ID|Email ID to read|345|
|Session|Gmail session|Default|
|Path for download attachment|Path where save the attachments|C:/User/Desktop|

### Close Server
  
Close server connection
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session to use|session1|
