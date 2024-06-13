import os

# print(dir(os))

# Ottenere la directory di lavoro corrente:
# directory_corrente = os.getcwd()
# print("La directory di lavoro corrente è:", directory_corrente)

# # Creare una nuova directory:
# nuova_directory = "nuova_cartella"
# os.mkdir(nuova_directory)
# print("Creata una nuova cartella chiamata", nuova_directory)

# # Eliminare una directory vuota:
# directory_da_elim = "nuova_cartella"
# os.rmdir(directory_da_elim)
# print("Eliminata la cartella", directory_da_elim)

# # Listare i file e le cartelle in una directory:
# directory = "."
# contenuto = os.listdir(directory)
# print("Contenuto della directory", directory, ":", contenuto)

# Controllare l'esistenza di un file o una directory
# file_da_verificare = "files.txt"
# if os.path.exists(file_da_verificare):
#   print("Il file", file_da_verificare, "esiste.")
# else:
#   print("Il file", file_da_verificare, "non esiste.")

# Controllare se è un file
percorso_file = 'file.txt'
if os.path.isfile(percorso_file):
    print(f"Il percorso '{percorso_file}' esiste ed è un file.")
else:
    print(f"Il percorso '{percorso_file}' non esiste o non è un file.")

# Percorso della directory da verificare
percorso_directory = 'test'

# Verifica se il percorso è una directory
if os.path.isdir(percorso_directory):
    print(f"Il percorso '{percorso_directory}' esiste ed è una directory.")
else:
    print(f"Il percorso '{percorso_directory}' non esiste o non è una directory.")


# Percorso del file di cui si vuole conoscere la dimensione
percorso_file = 'file.txt'

# Verifica se il file esiste
if os.path.isfile(percorso_file):
    # Ottieni la dimensione del file in byte
    dimensione_file = os.path.getsize(percorso_file)
    print(f"La dimensione del file '{percorso_file}' è di {dimensione_file} byte.")
else:
    print(f"Il file '{percorso_file}' non esiste o non è un file.")



# Percorso del file da analizzare
percorso_file = 'file.txt'

# Usa os.path.splitext() per ottenere il nome del file e l'estensione
nome_file, estensione = os.path.splitext(percorso_file)

# Stampa il risultato
print("Percorso del file:", percorso_file)
print("Nome del file:", nome_file)
print("Estensione del file:", estensione)


# # Informazioni sulle variabili d'ambiente
# print(os.environ['PATH'])


