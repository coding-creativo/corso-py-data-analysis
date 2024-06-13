import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configmailtrap import MAILTRAP_HOST, MAILTRAP_PORT, MAILTRAP_USERNAME, MAILTRAP_PASSWORD

def invia_email():
    mittente = "NomeUtente <persona@example.com>"
    destinatario = "Destinatario <persona@example.com>"

    oggetto = "Ciao ciao"
    corpo = "Corpo del messaggio"

    msg = MIMEMultipart()
    msg['From'] = mittente
    msg['To'] = destinatario
    msg['Subject'] = oggetto

    # Aggiungi il corpo del messaggio
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
            server.starttls() #avvia una connessione TLS (Transport Layer Security) per una comunicazione sicura.
            server.login(MAILTRAP_USERNAME, MAILTRAP_PASSWORD)
            server.sendmail(mittente, destinatario, msg.as_string())
        print("Email inviata con successo tramite Mailtrap")
    except Exception as e:
        print("Errore durante l'invio dell'email:", e)

invia_email()
