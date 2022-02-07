# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import base64
from bs4 import BeautifulSoup
import email
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'gmail_suite' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from mailparser import mailparser
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

global get_credentials, mod_gmail_suite_sessions
SESSION_DEFAULT = "gmail"
# Initialize settings for the module here
try:
    if not mod_gmail_suite_sessions:
        mod_gmail_suite_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_gmail_suite_sessions = {SESSION_DEFAULT: {}}


def get_msg_attach(file):
    import mimetypes
    from email.mime.base import MIMEBase
    from email.mime.nonmultipart import MIMENonMultipart
    from email import encoders
    content_type, encoding = mimetypes.guess_type(file)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'

    # print("content_type", content_type)
    # exit()
    main_type, sub_type = content_type.split('/', 1)

    if main_type == 'text':
        fp = open(file, 'rb')
        msg = MIMEText(fp.read().decode("utf-8"), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(file, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(file, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(file, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        encoders.encode_base64(msg)
        fp.close()
    return msg


def create_message(sender, to_, cc_, bcc_, subject_, message_text, filenames_):
    global get_msg_attach, MIMEMultipart, MIMEText, base64
    message = MIMEMultipart()
    message.attach(MIMEText(message_text, 'html'))
    message['to'] = to_
    message['cc'] = cc_
    message['bcc'] = bcc_
    message['from'] = sender
    message['subject'] = subject_

    for file in filenames_:
        filename_ = os.path.basename(file)

        msg_ = get_msg_attach(file)
        msg_.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename_))

        message.attach(msg_)

    raw_message = base64.urlsafe_b64encode(message.as_bytes())
    return {
        'raw': raw_message.decode("utf-8")
    }


class GmailSuite:
    global InstalledAppFlow, pickle, Request

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.send',
              'https://www.googleapis.com/auth/gmail.readonly']

    def __init__(self, credentials_path, user_id, session):
        self.credentials = self.set_credentials(credentials_path, session)
        self.user_id = user_id

    #@property
    def get_credentials(self, session):
        creds = None
        session_pickle = session + ".pickle"
        if os.path.exists(session_pickle):
            with open(session_pickle, 'rb') as token:
                creds = pickle.load(token)
        self._credentials = creds
        return creds
        #return self._credentials

    #@credentials.setter
    def set_credentials(self, credentials_path, session):

        try:
            """Shows basic usage of the Gmail API.
                        Lists the user's Gmail labels.
                        """
            creds = None
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            session_pickle = session + ".pickle"
            if os.path.exists(session_pickle):
                with open(session_pickle, 'rb') as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_path, self.SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(session_pickle, 'wb') as token:
                    pickle.dump(creds, token)

            self._credentials = creds
        except Exception as e:
            PrintException()
            raise e


if module == "conf_mail":

    try:
        path = GetParams("path")
        var_ = GetParams("var_")
        email = GetParams("from")
        session = GetParams("session")
        if not session:
            session = SESSION_DEFAULT
        print(session)
        gmail_suite = GmailSuite(path, email, session)
        service = build('gmail', 'v1', credentials=gmail_suite.get_credentials(session))
        mod_gmail_suite_sessions[session] = {
                "service": service,
                "gmail": gmail_suite
        }
        SetVar(var_, True)
    except Exception as e:
        PrintException()
        SetVar(var_, False)

        raise e

if module == "send_mail":
    to = GetParams('to')
    subject = GetParams('subject')
    body_ = GetParams('body')
    cc = GetParams('cc')
    bcc = GetParams('bcc')
    attached_file = GetParams('attached_file')
    files = GetParams('attached_folder')
    session = GetParams("session")
    if not session:
            session = SESSION_DEFAULT
    service = mod_gmail_suite_sessions[session]["service"]
    gmail_suite = mod_gmail_suite_sessions[session]["gmail"]
    filenames = [attached_file] if attached_file else []

    try:
        if files:
            for f in os.listdir(files):
                f = os.path.join(files, f)

                filenames.append(f)

        msg = create_message(gmail_suite.user_id, to, cc, bcc, subject, body_, filenames)
        sent = service.users().messages().send(userId='me', body=msg).execute()

        print('Message Id: %s' % sent['id'])

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_mail":
    filter_ = GetParams('filtro')
    var_ = GetParams('var_')
    label_id = GetParams('label_id')
    session = GetParams("session")
    order_by = GetParams("order_by")
    if not session:
            session = SESSION_DEFAULT
    try:
        service = mod_gmail_suite_sessions[session]["service"]
        gmail_suite = mod_gmail_suite_sessions[session]["gmail"]
        #service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        mails = service.users().messages().list(userId='me', q=filter_, labelIds=label_id).execute()
        
        list_ = []
        if "messages" in mails:
            list_ = [mail["id"] for mail in mails["messages"]]
        
        if order_by == "old":
            list_ = list_[::-1]

        SetVar(var_, list_)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "forward":
    id_ = '17d9f1b190f48c5e'
    #var_ = GetParams('var_')
    att_folder = ''
    session = 'nicolas'

    if not session:
            session = SESSION_DEFAULT
    service = mod_gmail_suite_sessions[session]["service"]
    gmail_suite = mod_gmail_suite_sessions[session]["gmail"]
    try:

        message = service.users().messages().get(userId='me', id=id_, format='full').execute()
        mime_message = service.users().messages().get(userId='me', id=id_, format='raw').execute()
        msg_str = base64.urlsafe_b64decode(mime_message['raw'].encode("utf-8")).decode("utf-8")
        mail_ = mailparser.parse_from_string(msg_str)
        nameFile = []

        if "parts" in message['payload']:
            for part in message['payload']['parts']:
                if part['filename'] and part['body'] and part['body']['attachmentId'] and att_folder:
                    attachment = service.users().messages().attachments().get(id=part['body']['attachmentId'],
                                                                              userId='me', messageId=id_).execute()

                    file_data = base64.urlsafe_b64decode(attachment['data'].encode('utf-8'))
                    if not att_folder.endswith("/"):
                        att_folder += "/"
                    path = ''.join([att_folder, part['filename']])

                    with open(path, 'wb') as f:
                        f.write(file_data)

        bs = ""
        bs_mail = BeautifulSoup(mail_.body, 'html.parser')
        try:
            bs = bs_mail.body.get_text()
        except:
            bs = mail_.body
        bs = bs_mail.body
        if "--- mail_boundary ---" in bs.__str__():
            html_list = bs.split("--- mail_boundary ---")
            html = BeautifulSoup(html_list[1], 'html.parser').get_text()
            html_list[1] = html
            bs = "\n".join(html_list)

        links = [{a.get_text(): a["href"] for a in bs_mail.find_all("a") if "href" in a}]

        final = {"date": mail_.date.__str__(), 'subject': mail_.subject,
                 'from': ", ".join([b for (a, b) in mail_.from_]),
                 'to': ", ".join([b for (a, b) in mail_.to]), 'cc': ", ".join([b for (a, b) in mail_.cc]), 'body': bs,
                 'files': nameFile, 'links': links}

        print("final", final)
        body = {
            "removeLabelIds": ['UNREAD']
        }

        message = service.users().messages().modify(userId='me', id=id_, body=body).execute()

        filenames = []
        to = 'nick.sfra.7@gmail.com'
        cc=''
        bcc=''
        subject=''
        msg = create_message(gmail_suite.user_id, to, cc, bcc, subject, bs, filenames)
        sent = service.users().messages().send(userId='me', body=msg).execute()

        print('Message Id: %s' % sent['id'])
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e


if module == "get_unread":
    filter_ = GetParams('filtro')
    var_ = GetParams('var_')
    session = GetParams("session")
    folder = GetParams("folder")
    order_by = GetParams("order_by")
    
    if not folder:
            folder = "inbox"
            
    if not session:
            session = SESSION_DEFAULT
    try:
        service = mod_gmail_suite_sessions[session]["service"]
        filter_ = "label:unread " + str(filter_) + f" in:{folder}" if filter_ else f"label:unread in:{folder}" 
        mails = service.users().messages().list(userId='me', q=filter_).execute()
        
        list_ = []
        if "messages" in mails:
            list_ = [mail["id"] for mail in mails["messages"]]

        if order_by == "old":
            list_ = list_[::-1]

        SetVar(var_, list_)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "read_mail":
    id_ = GetParams('id_')
    var_ = GetParams('var_')
    att_folder = GetParams('att_folder')
    session = GetParams("session")
    if not session:
            session = SESSION_DEFAULT
    service = mod_gmail_suite_sessions[session]["service"]
    gmail_suite = mod_gmail_suite_sessions[session]["gmail"]
    try:

        message = service.users().messages().get(userId='me', id=id_, format='full').execute()
        mime_message = service.users().messages().get(userId='me', id=id_, format='raw').execute()
        msg_str = base64.urlsafe_b64decode(mime_message['raw'].encode("utf-8")).decode("utf-8")
        mail_ = mailparser.parse_from_string(msg_str)
        nameFile = []

        if "parts" in message['payload']:
            for part in message['payload']['parts']:
                if part['filename'] and part['body'] and part['body']['attachmentId'] and att_folder:
                    attachment = service.users().messages().attachments().get(id=part['body']['attachmentId'],
                                                                              userId='me', messageId=id_).execute()

                    file_data = base64.urlsafe_b64decode(attachment['data'].encode('utf-8'))
                    if not att_folder.endswith("/"):
                        att_folder += "/"
                    path = ''.join([att_folder, part['filename']])

                    with open(path, 'wb') as f:
                        f.write(file_data)

        bs = ""
        bs_mail = BeautifulSoup(mail_.body, 'html.parser')
        try:
            bs = bs_mail.body.get_text()
        except:
            bs = mail_.body

        if "--- mail_boundary ---" in bs.__str__():
            html_list = bs.split("--- mail_boundary ---")
            html = BeautifulSoup(html_list[1], 'html.parser').get_text()
            html_list[1] = html
            bs = "\n".join(html_list)

        # bs = BeautifulSoup(mail_.body, 'html.parser').body.get_text()
        links = [{a.get_text(): a["href"] for a in bs_mail.find_all("a") if "href" in a}]

        final = {"date": mail_.date.__str__(), 'subject': mail_.subject,
                 'from': ", ".join([b for (a, b) in mail_.from_]),
                 'to': ", ".join([b for (a, b) in mail_.to]), 'cc': ", ".join([b for (a, b) in mail_.cc]), 'body': bs,
                 'files': nameFile, 'links': links}

        SetVar(var_, final)
        body = {
            "removeLabelIds": ['UNREAD']
        }

        message = service.users().messages().modify(userId='me', id=id_, body=body).execute()
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e


if module == "create_folder":
    try:
        folder_name = GetParams('folder_name')
        session = GetParams("session")
        if not session:
            session = SESSION_DEFAULT
        service = mod_gmail_suite_sessions[session]["service"]
        gmail_suite = mod_gmail_suite_sessions[session]["gmail"]
        body = {
            "labelListVisibility": 'labelShow',
            "messageListVisibility": 'show',
            "name": folder_name
        }

        mails = service.users().labels().create(userId='me', body=body).execute()

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "move_mail":
    # imap = GetGlobals('email')
    id_ = GetParams("id_")
    label_ = GetParams("label_")
    var = GetParams("var")
    session = GetParams("session")
    if not session:
            session = SESSION_DEFAULT
    service = mod_gmail_suite_sessions[session]["service"]
    gmail_suite = mod_gmail_suite_sessions[session]["gmail"]
    if not id_:
        raise Exception("No ha ingresado ID de email a mover")
    if not label_:
        raise Exception("No ha ingresado carpeta de destino")

    try:
        # Create gmail service
        #service = build('gmail', 'v1', credentials=gmail_suite.credentials)

        # Get all labels and filter by name
        labels = service.users().labels().list(userId='me').execute()["labels"]

        label = None
        for lbl in labels:
            if lbl["name"] == label_:
                label = lbl
                break

        # Create body, add label and remove from inbox

        if label is not None:
            body = {
                "addLabelIds": [label["id"]],
                "removeLabelIds": ["INBOX"]
            }
            service.users().messages().modify(userId='me', id=id_, body=body).execute()
            SetVar(var, True)
        else:
            SetVar(var, False)

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        SetVar(var, False)
        raise e

if module == "markAsUnread":
    id_ = GetParams("id_")
    var = GetParams("var")  
    session = GetParams("session")
    if not session:
            session = SESSION_DEFAULT
    service = mod_gmail_suite_sessions[session]["service"]
    gmail_suite = mod_gmail_suite_sessions[session]["gmail"]
    try:
        body = {
            "addLabelIds": ['UNREAD']
        }
        #service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        message = service.users().messages().modify(userId='me', id=id_, body=body).execute()

    except Exception as e:
        PrintException()
        raise e
            
if module == "close":
    session = GetParams("session")
    if not session:
            session = SESSION_DEFAULT
    mod_gmail_suite_sessions[session]["service"] = None
    mod_gmail_suite_sessions[session]["gmail"] = None


if module == "listLabels":
    var_ = GetParams('var_')
    try:
        session = GetParams("session")
        if not session:
            session = SESSION_DEFAULT
        service = mod_gmail_suite_sessions[session]["service"]
        gmail_suite = mod_gmail_suite_sessions[session]["gmail"]
        #service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        labels = service.users().labels().list(userId='me').execute()
        label_id_list = []
        for label in labels['labels']:
            label_id_list.append(label['id'])
        SetVar(var_, label_id_list)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
