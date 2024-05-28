lotes = []
for i in range(5):
    lotes.append(int(input("Introduzca un número ganador: ")))
lotes.sort()
print(f"Los numeros ganadores son: {lotes}")