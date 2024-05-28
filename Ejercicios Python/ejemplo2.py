opcion = 0
while opcion != 5:
    print("Goshujinsama ¿Qué operación desea realizar-nya?") # mensaje de inicio
    # opciones a elegir
    print("1. Suma.")
    print("2. Resta.")
    print("3. Multiplicación.")
    print("4. División.")
    print("5. Salir ohnyo ówò")
    # defino la opcion como variable y lee la respuesta
    opcion = int(input(">> " ))
    if opcion == 1:
        num1=float(input("Ingrese el primer numero Goshujinsama: "))
        num2=float(input("Ingrese el segundo numero nya: "))
        print("La suma total es de ", num1+num2, " desu nya.")
    elif opcion == 2:
        num1=float(input("Ingrese el primer numero Goshujinsama: "))
        num2=float(input("Ingrese el segundo numero nya: "))
        print("La suma total es de ", num1-num2, " desu nya.")
    elif opcion == 3:
        num1=float(input("Ingrese el primer numero Goshujinsama: "))
        num2=float(input("Ingrese el segundo numero nya: "))
        print("La suma total es de ", num1*num2, " desu nya.")
    elif opcion == 4:
        num1=float(input("Ingrese el primer numero Goshujinsama: "))
        num2=float(input("Ingrese el segundo numero nya: "))
        print("La suma total es de ", num1/num2, " desu nya.")
    elif opcion == 5:
        print("Gracias por usarme Goshujinsama ¡Nos veremos pronto!")