import os
from dotenv import load_dotenv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

logging.basicConfig(filename='mail_log.txt', level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

load_dotenv()

def go_mail(mail, data_struc):
    try:
        mail_sender = os.getenv('SENDER_MAIL')
        password = os.getenv('MAIL_PASS')
        mail_receiver = mail

        message = MIMEMultipart("alternative")
        message['Subject'] = 'News specially choose for you'
        message['From'] = mail_sender
        message['To'] = mail_receiver

        html_format_message = htmlPage(data_struc)
        message_as_object = MIMEText(html_format_message, "html")
        message.attach(message_as_object)

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(mail_sender, password)
        s.send_message(message)

        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        #     server.login(mail_sender, password)
        #     server.sendmail(mail_sender, mail_receiver, message.as_string())

        print("Message sent")
        logging.info("[MAIL] Mail has been sent to  %s ", (mail_receiver) )
        check_mail = "success"
        return check_mail
    
    except (Exception,TypeError,smtplib.SMTPException) as e:
        print("An error occured during the sent of an email :", e)
        logging.info("[MAIL]Fail to send mail to %s message error:  %s", (mail_receiver,e))
        #conversion du message d'erreur en string
        check_mail = str(e)
        return check_mail

def table_data(my_tuple):
    #initialisation du tableau
    row =''
    for i in range (len(my_tuple)):
        row +="<tr>"
        row += f'<td>{my_tuple[i][1]}</td>'
        row += f'<td>{my_tuple[i][2]}</td>'
        row += f'<td>{my_tuple[i][3]}</td>'
        row += f'<td>{my_tuple[i][4]}</td>'
        row += f'</tr>\n'
    return row

def htmlPage (my_tuple):
    header = """
    <html>
            <head>
            <h1 style="color: #5e9ca0; text-align: left;">T'es dans le complot !!!</h1>
            
            <style type="text/css">
                table {
                    background: white;
                    border-radius:3px;
                    border-collapse: collapse;
                    height: auto;
                    max-width: 900px;
                    padding:5px;
                    width: 100%;
                    animation: float 5s infinite;
                }
                th {
                    color:#D5DDE5;;
                    background:#1b1e24;
                    border-bottom: 4px solid #9ea7af;
                    font-size:14px;
                    font-weight: 300;
                    padding:10px;
                    text-align:center;
                    vertical-align:middle;
                }
                tr {
                    border-top: 1px solid #C1C3D1;
                    border-bottom: 1px solid #C1C3D1;
                    border-left: 1px solid #C1C3D1;
                    color:#666B85;
                    font-size:16px;
                    font-weight:normal;
                }
                tr:hover td {
                    background:#4E5066;
                    color:#FFFFFF;
                    border-top: 1px solid #22262e;
                }
                td {
                    background:#FFFFFF;
                    padding:10px;
                    text-align:left;
                    vertical-align:middle;
                    font-weight:300;
                    font-size:13px;
                    border-right: 1px solid #C1C3D1;
                }
            </style>
            </head>
            <body>
            <table>
            <thead>
                <tr>
                    <th>Titre</th>
                    <th>Image</th>
                    <th>Contenue</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
    """


        
    footer = """
            </tbody>
            </table> 
        </body>
    </html>"""

    html = header + table_data(my_tuple) + footer

    return html
