# Como usar este modulo

*Read this in other languages: [English](how_to_use.md), [Portugues](how_to_use.pr.md), [Español](how_to_use.es.md).*

Para trabalhar com este módulo é necessário ativar a API do Gmail. Para isso, você deve seguir os seguintes passos.
* Ir para o [Google Console](https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard%3Fproject%3Dprueba-312216%26hl%3Des&folder=&organizationId=777182023349&hl=es) para criar um novo projeto (caso já tenha criado, pule esta etapa) e preencha os dados indicados no formulário

![](imgs/proyectonuevo.png)

Na barra superior você verá o nome do projeto. Caso não seja exibido, mude para o projeto criado clicando em no menu que está destacado na imagem.

![](imgs/seleccionarproyecto.png)

Se você receber a mensagem "Você não tem permissões suficientes para visualizar esta página". Conforme mostrado na imagem acima, clique em **API and Services** no painel esquerdo e, após mudar para a página, clique em **ENABLE API AND SERVICES**

![](imgs/habilitarapiyservicios.png)

No mecanismo de pesquisa "APIs e serviços de pesquisa", digite **Gmail API**. Em seguida, ative a API clicando em **Ativar**

![](imgs/gamialapi.png)

Levará um momento para carregar e a página será redirecionada para a página de configurações da API.

* Clique em **CRIAR CREDENCIAIS**, para criar as credenciais

![](imgs/crearcredenciales.png)

O primeiro passo é selecionar o tipo de credencial. Selecionamos **Gmail API** e marcamos a opção **User data**. Em seguida, clique em próximo.

![](imgs/tipocredencial.png)

Na tela de consentimento, digite um nome para o aplicativo e selecione um email.

![](imgs/pantallaconsentimiento.png)

Na tela de permissões, clique em **ADICIONAR OU REMOVER PERMISSÕES**. Um modal será aberto para selecionar as permissões. No tipo de filtro **Gmail API**, clique no menu suspenso **Linhas por página** e selecione **100** para ver todas as opções, selecione todas marcando **API** e clique em **Atualizar**.


![](imgs/agregarpermisos.png)

![](imgs/actualizar.png)

Depois que as permissões selecionadas forem adicionadas, clique em **SALVAR E CONTINUAR**

![](imgs/guardarycontinuar.png)

Por fim, na tela OAuth, selecione o tipo de aplicativo **Desktop APP** e adicione um nome. Finalizamos clicando em criar.

![](imgs/oauth.png)

Ele irá criar as credenciais para nós, clicamos em download e depois em pronto. É importante manter o arquivo baixado. Ele será usado posteriormente no módulo.

![](imgs/descargar.png)

No menu à esquerda, ao clicar em **Tela de consentimento**, caso você tenha uma conta corporativa do Gmail, poderá usar a API por tempo indeterminado e verá que o tipo de usuário é **Interno**. Se você tiver uma conta gratuita do Gmail, terá que dar consentimento uma vez por semana para poder se conectar à sua conta de e-mail e verá que seu tipo de usuário é **Externo** e terá que adicionar usuários de teste.

![](imgs/interno.png)

![](imgs/externo.png)

Para evitar cometer todas as semanas, você pode publicar o aplicativo para aprovação do Google e usá-lo indefinidamente.