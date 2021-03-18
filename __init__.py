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

global gmail_suite


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


def create_message(sender, to_, cc_, subject_, message_text, filenames_):
    global get_msg_attach, MIMEMultipart, MIMEText, base64
    message = MIMEMultipart()
    message.attach(MIMEText(message_text, 'html'))
    message['to'] = to_
    message['cc'] = cc_
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

    def __init__(self, credentials_path, user_id):
        self.credentials = credentials_path
        self.user_id = user_id

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, credentials_path):

        try:
            """Shows basic usage of the Gmail API.
                        Lists the user's Gmail labels.
                        """
            creds = None
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('gmail.pickle'):
                with open('gmail.pickle', 'rb') as token:
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
                with open('gmail.pickle', 'wb') as token:
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

        gmail_suite = GmailSuite(path, email)
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
    attached_file = GetParams('attached_file')
    files = GetParams('attached_folder')
    filenames = [attached_file] if attached_file else []

    try:
        if files:
            for f in os.listdir(files):
                f = os.path.join(files, f)
                print(f)
                filenames.append(f)
        print(filenames)
        service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        msg = create_message(gmail_suite.user_id, to, cc, subject, body_, filenames)
        sent = service.users().messages().send(userId='me', body=msg).execute()
        print(sent)
        print('Message Id: %s' % sent['id'])

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_mail":
    filter_ = GetParams('filtro')
    var_ = GetParams('var_')
    label_id = GetParams('label_id')
    try:
        service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        mails = service.users().messages().list(userId='me', q=filter_, labelIds=label_id).execute()
        if "messages" in mails:
            list_ = [mail["id"] for mail in mails["messages"]]
        else:
            list_ = []

        SetVar(var_, list_)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_unread":
    filter_ = GetParams('filtro')
    var_ = GetParams('var_')

    try:
        service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        filter_ = "label:unread" + str(filter_) if filter_ else "label:unread"
        mails = service.users().messages().list(userId='me', q=filter_).execute()

        if "messages" in mails:
            list_ = [mail["id"] for mail in mails["messages"]]
        else:
            list_ = []

        SetVar(var_, list_)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "read_mail":
    id_ = GetParams('id_')
    var_ = GetParams('var_')
    att_folder = GetParams('att_folder')

    try:

        service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        message = service.users().messages().get(userId='me', id=id_, format='metadata').execute()
        mime_message = service.users().messages().get(userId='me', id=id_, format='raw').execute()
        msg_str = base64.urlsafe_b64decode(mime_message['raw'].encode("utf-8")).decode("utf-8")
        mail_ = mailparser.parse_from_string(msg_str)
        nameFile = []

        if "parts" in message['payload']:
            for part in message['payload']['parts']:
                if part['filename'] and part['body'] and part['body']['attachmentId']:
                    attachment = service.users().messages().attachments().get(id=part['body']['attachmentId'],
                                                                              userId='me', messageId=id_).execute()

                    file_data = base64.urlsafe_b64decode(attachment['data'].encode('utf-8'))
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
        links = [{a.get_text(): a["href"] for a in bs_mail.find_all("a")}]

        print(mail_, dir(mail_))
        final = {"date": mail_.date.__str__(), 'subject': mail_.subject,
                 'from': ", ".join([b for (a, b) in mail_.from_]),
                 'to': ", ".join([b for (a, b) in mail_.to]), 'cc': ", ".join([b for (a, b) in mail_.cc]), 'body': bs,
                 'files': nameFile, 'links': links}

        SetVar(var_, final)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

# if module == "reply_email":
#     id_ = GetParams('id_')
#     body_ = GetParams('body')
#     attached_file = GetParams('attached_file')
#     # print(body_, attached_file)
#
#     try:
#         mail = imaplib.IMAP4_SSL('imap.gmail.com')
#         mail.login(fromaddr, password)
#         mail.select("inbox")
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(fromaddr, password)
#
#         # mail.select()
#         typ, data = mail.fetch(id_, '(RFC822)')
#         raw_email = data[0][1]
#         mm = email.message_from_bytes(raw_email)
#
#         # msg = MIMEMultipart()
#         # msg.attach(MIMEText(body_, 'plain'))
#
#         #    m_ = create_auto_reply(mm, body_)
#         mail__ = MIMEMultipart()
#         mail__['Message-ID'] = make_msgid()
#         mail__['References'] = mail__['In-Reply-To'] = mm['Message-ID']
#         mail__['Subject'] = 'Re: ' + mm['Subject']
#         mail__['From'] = mm['To'] = mm['Reply-To'] or mm['From']
#         mail__.attach(MIMEText(dedent(body_), 'html'))
#
#         if attached_file:
#             if os.path.exists(attached_file):
#                 filename = os.path.basename(attached_file)
#                 attachment = open(attached_file, "rb")
#                 part = MIMEBase('application', 'octet-stream')
#                 part.set_payload((attachment).read())
#                 attachment.close()
#                 encoders.encode_base64(part)
#                 part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#                 mail__.attach(part)
#
#         # print("FROMADDR",fromaddr, "FROM",mm['From'], "TO:",mm['To'])
#         server.sendmail(fromaddr, mm['From'], mail__.as_bytes())
#         # server.sendmail(fromaddr, mm['To'], mail__.as_bytes())
#         # server.close()
#         mail.logout()
#     except Exception as e:
#         PrintException()
#         raise e

if module == "create_folder":
    try:
        folder_name = GetParams('folder_name')
        service = build('gmail', 'v1', credentials=gmail_suite.credentials)
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

    if not id_:
        raise Exception("No ha ingresado ID de email a mover")
    if not label_:
        raise Exception("No ha ingresado carpeta de destino")

    try:
        # Create gmail service
        service = build('gmail', 'v1', credentials=gmail_suite.credentials)

        # Get all labels and filter by name
        labels = service.users().labels().list(userId='me').execute()["labels"]

        label = None
        for lbl in labels:
            if lbl["name"] == label_:
                label = lbl
                break

        # Create body, add label and remove from inbox
        print(label)
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

    try:
        body = {
            "addLabelIds": ['UNREAD']
        }
        service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        message = service.users().messages().modify(userId='me', id=id_, body=body).execute()
        print(message)
    except Exception as e:
        PrintException()
        raise e

if module == "close":
    gmail_suite = None

if module == "listLabels":
    var_ = GetParams('var_')
    try:
        service = build('gmail', 'v1', credentials=gmail_suite.credentials)
        labels = service.users().labels().list(userId='me').execute()
        label_id_list = []
        for label in labels['labels']:
            label_id_list.append(label['id'])
        SetVar(var_, label_id_list)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e