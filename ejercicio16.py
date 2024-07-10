# Importamos el modulo random
import random

# Generamos 5 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for var in range(5)]

print("Los 5 números aleatorios son:")
for i, num in enumerate(numeros_aleatorios, 1):
    print(f"Número {i}: {num}")