import datetime

# Data corrente
oggi = datetime.date.today()
print("Oggi:", oggi)

# Data specifica
data_specifica = datetime.date(1912, 6, 23)
print("Data specifica:", data_specifica)

# Ora specifica
ora_specifica = datetime.time(14, 30, 45)
print("Ora specifica:", ora_specifica)

# Data e ora corrente
adesso = datetime.datetime.now()
print("Adesso:", adesso)

# Ottieniamo il timestamp
timestamp = adesso.timestamp()
print("Timestamp:", timestamp)


