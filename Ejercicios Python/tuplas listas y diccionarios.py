# tupla: permite almacenar dator INMUTABLES, es decir, una vez creados no se puede modificar.

tupla = (1, False, "hi", 2309)

# lista: se pueden modificar, agregar y eliminar datos

lista = [29, True, 3.14, "aloha", 23]
print(lista)

print(lista[1:3]) #se pueden imprimir varios valores a la vez

lista[4] = "not funny anymore" #se pueden cambiar atributo

lista[3] = [3, 2, 1] #también se pueden crear listas dentro de listas

lista.append(3) #permite agregar un elemento al final de la lista

print(lista.count(29)) #cuenta el número de veces que se repite un elemento

print(lista.index(29)) #muestra la posición del primer elemento que contenga

# diccionario: los valores almacenados se asocian a un nombre clave, a diferencia de las listas/tuplas que se asocian a un valor numérico

diccionario = {1:"uno", 2:"dos"}

diccionario[3] = "tres" #se puede agregar también desde fuera

lista1=[10,7,3,7,2]
suma=0
x=0
while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1
print("Los elementos de la lista son")
print(lista1)
print("La suma de todos los elementos es")
print(suma)

meses = ["enero","febrero","marzo","abril"]
print(meses[0])
print(meses[3])

lista2=[10,20,30]
print(len(lista2))
lista2.append(100)
print(len(lista2))
print(lista2[0])
print(lista2[3])
100

lista3=[]
for z in range(5):
    valor=int(input("Ingrese un valor entero: "))
lista3.append(valor)
print(lista3)

nombres=[]
edades=[]
for y in range(5):
    nom=input("Ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed=int(input("Ingrese la edad: "))
    edades.append(ed)
print("Nombres de las personas mayores de edad: ")
for y in range(5):
    if edades[y]>= 18:
        print(nombres[y])  

sueldos=[]
for a in range(5):
    valor=int(input("Ingrese sueldo: "))
    sueldos.append(valor)
print("Lista sin ordenar: ")
print(sueldos)
for a in range(4):
    if sueldos[a]>sueldos[a+1]:
        aux=sueldos[a]
        sueldos[a]=sueldos[a+1]
        sueldos[a+1]=aux
print("lista con el último elemento ordenado: ")
print(sueldos)

lista4=[10,20,30,40,50]
print(lista4)
lista4.pop(0) #pop se usa para eliminar valores almacenados en una lista
lista4.pop(1)
lista4.pop(2)
print(lista4)

