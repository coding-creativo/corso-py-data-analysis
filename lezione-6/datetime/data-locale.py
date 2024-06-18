import locale
from datetime import datetime

# Imposta la localizzazione italiana
locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')

# Ottieni la data e ora attuali
oggi = datetime.now()
print(oggi)

# Formatta la data in italiano
data_formattata = oggi.strftime("%A %d %B %Y %H:%M:%S")

# Stampa la data formattata
print("Data formattata in italiano:", data_formattata)


