with open('output.txt', 'w') as file:
    file.write('Ciao a tutti!\n')  # Scrive una stringa nel file

with open('frutta.txt', 'w') as file:
    data = ['mela', 'banana', 'pera']
    for item in data:
        file.write(item + '\n')  # Scrive una lista di elementi nel file


with open('persona.txt', 'w') as file:
    person = {
        'name': 'Alice',
        'age': 30,
        'city': 'Wonderland'
    }
    for key, value in person.items():
        file.write(f'{key}: {value}\n')

# scrivere da un file di input ad un altro
input_file = 'frutta.txt'
output_file = 'output_copy.txt'

with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
    for line in f_input:
        f_output.write(line)

### copiare il contenuto di un file in un altro file
# input_file = 'frutta.txt'
# output_file = 'output_copy-2.txt'

# with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
#     # Leggi tutte le linee dal file di input e rimuovi il carattere di nuova riga
#     lines = [line.strip() for line in f_input.readlines()]

#     # Scrivi tutte le linee su una singola riga nel file di output
#     f_output.write(' '.join(lines))




    