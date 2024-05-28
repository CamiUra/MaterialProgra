cursos = ["Matemáticas","Física","Historia","Lengua"]
notas = []
for curso in cursos:
    nota = input("Ingrese su nota de " +curso+ ": ")
    notas.append(nota)
for i in range(len(cursos)):
    print("En " + cursos[i] + " has sacado " + notas[i])