print("Bienvenido a nuestro menú online.")
while True:
    print("""Por favor, selecciones una de las siguientes opciones:
          1.- Comenzar el programa.
          2.- Mostrar el menú.
          3.- Cerrar el programa.
          """)
    opcion = int(input(">>> "))
    if opcion == 1:
        print("¡Comenzamos!")
    elif opcion == 2:
        print("""El menú es el siguiente:
        -Puré con acompañamiento.
        -Fideos con salsa bolognesa.
        -Lomo a lo pobre.
        """)
    elif opcion > 3:
        print("Opcion inválida")
    elif opcion == 3:
        print("¡Gracias por usar nuestro menú online!")
        break