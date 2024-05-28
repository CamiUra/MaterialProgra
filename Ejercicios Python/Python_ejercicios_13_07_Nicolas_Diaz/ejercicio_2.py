tupla = (1,2,3,4,5,6,7,8,9,10)
x = int(input("Seleccione el índice de la tupla que desea observar: "))
if x < len(tupla): #Si X es MENOR QUE EL LARGO DE LA TUPLA
    ind = tupla[x] #El índice será lo que seleccionemos atrás
    print(f'El índice de la tupla es: {ind}')
else:
    print("El valor no se encuentra en la tupla")