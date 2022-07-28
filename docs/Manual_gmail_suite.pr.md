# Gmail G Suite
  
Módulo para realizar ações no Gmail 

*Read this in other languages: [English](Manual_gmail_suite.md), [Portugues](Manual_gmail_suite.pr.md), [Español](Manual_gmail_suite.es.md).*

*How to use: [English](/docs/how_to_use.md), [Portugues](/docs/how_to_use.pr.md), [Español](/docs/how_to_use.es.md).*
  
![banner](/docs/imgs/Banner_gmail_suite.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot.  



## Descrição do comando

### Configuração do servidor
  
Configure o servidor de email a ser usado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Credenciais|Caminho do arquivo json baixado na etapa anterior|credentials.json|
|Usuário|E-mail que será usado para enviar e-mails. Pode ficar em branco se você não quiser enviar e-mail.|user@example.com|
|Sessão|Nome da sessão que vamos atribuir|session1|
|Atribuir resultado à variável|Resultado da conexão|Variável|

### Enviar Email
  
Envia um email, você deve configurar previamente o servidor
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão a ser usada|session1|
|Para|Destinatários da mensagem. Devem ser separados por vírgulas|to@mail.com, to2@mail.com|
|Copia|Destinatários enviados por cópia. Devem ser separado por vírgula|cc@mail.com, cc2@mail.com|
|Cópia Oculta|Destinatários enviados por cópia oculta. Devem ser separado por vírgula|bcc@mail.com, bcc2@mail.com|
|Assunto|Assunto da mensagem|Nuevo mail|
|Mensajem|Corpo do e-mail. tags html podem ser usadas|Hi from Rocketbot!|
|Arquivo anexo|Caminho do arquivo a ser anexado|C:\User\Desktop\test.txt|
|Pasta (vários arquivos)|Caminho da pasta com os arquivos a serem anexados|C:\User\Desktop\Files|

### Listar todos os e-mails
  
Liste todos os e-mails, você pode especificar um filtro
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro|Você pode usar todas as opções de filtro do Gmail.|subject:COMPRA|
|Pasta|Pasta de onde todos os emails não estão listados|INBOX|
|Sessão|Nome da sessão a ser usada|session1|
|Organizar por|Classifique os emails listados pelo parâmetro desejado|New First|
|Atribuir à variável|Nome da variável onde a lista de e-mail será salva|Variável|

### Lista de e-mail não lida
  
Listar e-mails não lidos, você pode especificar um filtro
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro|Você pode usar todas as opções de filtro do Gmail|subject:COMPRA|
|Pasta|Especifique o nome da pasta de onde você deseja obter os e-mails, por padrão, caixa de entrada|inbox|
|Sessão|Nome da sessão a ser usada|session1|
|Organizar por|Classifique os emails listados pelo parâmetro desejado|New First|
|Atribuir à variável|Nome da variável onde a lista de e-mail será salva|Variável|

### Ler email por ID
  
Você pode especificar o ID de um email para lê-lo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do email|Id obtido nos comandos para listar email|345|
|Sessão|Nome da sessão a ser usada|session1|
|Atribuir à variável|Nome da variável onde o conteúdo do e-mail lido será salvo|Variável|
|Caminho para baixar anexos|Caminho da pasta onde os anexos serão salvos|C:\User\Desktop|

### Criar marcador
  
Você pode criar um marcador com o nome que quiser
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da marcador|Nome do marcador a ser criada|Digite o nome do marcador|
|Sessão|Nome da sessão a ser usada|session1|

### Mover e-mail para marcador
  
Mover e-mail de um marcador para outro
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do email|Id obtido nos comandos para listar email|1afr547edfds|
|Nome da etiqueta|Marcador para onde o e-mail será movido|test|
|Sessão|Nome da sessão a ser usada|session1|
|Atribuir resultado à variável|Variável onde será salvo. True se o email foi movido. Caso contrário, retornará False|Variável|

### Marcar e-mail como não lido
  
Qualquer email aberto anteriormente pode ser marcado como não lido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do email|Id obtido nos comandos para listar email|1afr547edfds|
|Sessão|Nome da sessão a ser usada|session1|

### Listar todos os marcadores
  
Obtenha uma lista de todos os marcadores de correio e armazene-as em uma variável
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão a ser usada|session1|
|Listar todos os dados|Obtém id, nome, visibilidade, etc. Se estiver desmarcado, ele só obtém o id|True|
|Atribuir à variável|Variável onde os marcadores serão salvos|Variável|

### Reenviar
  
Reenviar um email
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão a ser usada|session1|
|ID Mail|Id obtido nos comandos para listar email|321|
|Para|Destinatários da mensagem. Devem ser separados por vírgulas|to@mail.com, to2@mail.com|
|Copia|Destinatários enviados por cópia. Devem ser separados por vírgulas|cc@mail.com, cc2@mail.com|
|Copia Oculta|Destinatários enviados por cópia oculta. Devem ser separados por vírgulas|bcc@mail.com, bcc2@mail.com|
|Assunto|Assunto da mensagem|Novo mail|

### Baixar anexos por ID
  
Baixe anexos de e-mail e salve-os em uma pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do email|ID do email a leer|345|
|Sessão|Sessão de Gmail|Default|
|Caminho para baixar anexos|Caminho da pasta onde os anexos serão salvos|C:/User/Desktop|

### Fechar conexão
  
Feche a conexão do servidor
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão a ser usada|session1|
