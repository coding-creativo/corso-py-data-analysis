import random

# Generazione di numeri casuali
print(random.random())                # Output: Numero casuale in [0.0, 1.0)
print(random.randint(1, 100))         # Output: Numero casuale tra 1 e 100 inclusi
print(random.uniform(1.5, 2.5))       # Output: Numero casuale tra 1.5 e 2.5
print(random.randrange(10))           # Output: Numero casuale tra 0 e 9 inclusi
print(random.randrange(0, 10, 2))     # Output: Numero casuale tra 0 e 9 inclusi, passo 2

# Scelta casuale da una sequenza
numbers = [1, 2, 3, 4, 5]
print(random.choice(numbers))        # Output: Elemento casuale da numbers
print(random.choice(['mela', 'banana', 'pera'])) # Output: Elemento casuale da una lista

random.shuffle(numbers)               # Mescola numbers in modo casuale
print(numbers)                        # Output: Lista numbers mescolata casualmente

# Estrazione di un campione casuale da una sequenza 
sample_numbers = random.sample(numbers, 3) 
print(sample_numbers) # Output: Campione casuale di 3 elementi dalla lista numbers