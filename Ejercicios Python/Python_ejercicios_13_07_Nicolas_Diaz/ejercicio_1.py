import random

numeros = []
for x in range(10):
    numero = random.randint(1, 100)
    numeros.append(numero)

numeros.sort()

print("Números ordenados de menor a mayor:")
print(numeros)
