sum=0
n=0
while n != "gato":
    n=str(input("Ingrese la palabra <gato>: "))
    if n!="gato":
        print("Palabra incorrecta, escriba <gato>")
        sum=sum+1
    else:
        print("Ha ingresado la palabra incorrecta" ,sum, "veces.")
else:
    print("Saliendo del programa")