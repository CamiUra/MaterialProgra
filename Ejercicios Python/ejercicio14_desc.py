print("Bienvenido a su calculador de precio según cantidad.") #mensaje que saldrá solo la primera vez
opcion = 0
cantidad = 0
#establecer las variables en 0
while opcion != 2: #mientras no sea 2 el programa seguirá
    print("""¿Desea hacer un cálculo?
    1.- Si
    2.- No """)
    opcion = int(input(">>> ")) #leemos la entrada
    if opcion == 1:
        print("""Nuestra tienda ofrece los siguientes precios según la cantidad a comprar:
        - Entre 1 y 9 productos: $10
        - Entre 10 y 49 productos: $9
        - Entre 50 y 199 productos: $8
        - De 200 en adelante: $6
        """)
        cantidad = int(input("""Ingrese la cantidad que desea comprar 
        >>> """)) #leemos la cantidad
        #segun la cantidad ingresada se dará un precio y un descuento
        if cantidad < 10:
            print("El total a pagar es de " +"$" ,cantidad * 10)
        elif cantidad >=10 and cantidad < 50:
            print("El total a pagar es de " +"$" ,cantidad * 9)
            print("Se ha descontado un total de " +"$" ,cantidad * 10 - cantidad * 9)
        elif cantidad >= 50 and cantidad < 200:
            print("El total a pagar es de " +"$" ,cantidad * 8)
            print("Se ha descontado un total de " +"$" ,cantidad * 10 - cantidad*8)
        elif cantidad >= 200:
            print("EL precio a pagar es de " +"$" ,cantidad * 6)
            print("Se ha descontado un total de " +"$" ,cantidad * 10 - cantidad*6)
    elif opcion ==2:
        print("¡Gracias por usar nuestros servicios!")  