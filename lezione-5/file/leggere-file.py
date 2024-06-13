# with open('file.txt') as file:
#     content = file.readline()  # Legge una sola riga
#     print(content)
    
#per leggere tutto il contenuto del file possiamo usare
with open('files.txt') as file:
    content = file.read()  # Legge l'intero contenuto del file
    print(content)

# #oppure
with open('file.txt') as file:
    for line in file:  # Itera riga per riga
        print(line.strip())  # strip rimuove i caratteri di newline e spazi dalla riga