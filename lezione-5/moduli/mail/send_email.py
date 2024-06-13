import smtplib #Questo modulo fornisce le funzionalità per inviare email tramite il protocollo SMTP.
#  Importiamo i moduli dal pacchetto email.mime che consentono di costruire email con parti di testo e multipart, rispettivamente.
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from configmail import mittente, password, destinatario

# mittente = '...'
# password = '...'
# destinatario = '...'

''' Cos'è MIME?
########## MIME è uno standard che estende il formato dei messaggi di posta elettronica per supportare testo in vari formati carattere, allegati binari, immagini, audio, video e altri tipi di dati oltre al testo ASCII puro. È utilizzato per consentire la comunicazione di dati multimediali tramite protocolli di posta elettronica.

########## Multipart in un Messaggio MIME
#### Un messaggio email che utilizza il tipo di contenuto multipart può includere più parti:
# text/plain: Parte contenente testo semplice.
# text/html: Parte contenente testo formattato in HTML.
# image/jpeg, image/png: Parti contenenti immagini.
# application/pdf, application/octet-stream: Parti contenenti allegati binari come file PDF o altri tipi di file.
# Queste parti sono solitamente combinate all'interno di un unico messaggio email usando il tipo di contenuto multipart. Ogni parte ha un propria intestazione che specifica il tipo di contenuto (Content-Type) e, se necessario, altri metadati come la codifica (Content-Transfer-Encoding).
'''


oggetto = "Mail mandata con Python"
corpo = "Questa mail è mandata con Python"

msg = MIMEMultipart() #Crea un oggetto MIMEMultipart che rappresenta l'intero messaggio email.
msg['From'] = mittente
msg['To'] = destinatario
msg['Subject'] = oggetto
msg['Reply-To'] = mittente

msg.attach(MIMEText(corpo, 'plain')) # Aggiunge il corpo del messaggio email al messaggio multipartite utilizzando MIMEText con il tipo di contenuto plain

server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # Creiamo una connessione sicura SSL con il server SMTP di Gmail utilizzando il protocollo SMTP su SSL sulla porta 465.
server.login(mittente, password) # Effettua il login utilizzando le credenziali del mittente (indirizzo email e password). Nota: se usate l'autenticazione a due fattori, dovrete generare una "password per l'app" da utilizzare qui.
server.sendmail(mittente, destinatario, msg.as_string()) # Invia effettivamente il messaggio email, convertendo l'oggetto msg in una stringa formattata secondo il formato MIME richiesto dal server SMTP.
server.quit() #Chiudiamo la connessione con il server SMTP dopo aver inviato la mail.

# N.B. occorre permette l'accesso delle app esterne ed impostare la password su gmail nella sezione app password se avete attivato l'autenticazione a due fattori!!!

#verifica in due passaggi:
# https://support.google.com/accounts/answer/185839?hl=it

# Accedere con le password per le app
# https://support.google.com/accounts/answer/185833?hl=it


