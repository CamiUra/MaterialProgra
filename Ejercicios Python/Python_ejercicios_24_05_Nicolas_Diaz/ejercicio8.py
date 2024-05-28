edad=int(input("Ingrese su edad: "))
while edad >= 18:
    ing=int(input("Ingrese sus ingresos mensuales: "))
    if ing >= 400000:
        print("Usted debería abrir una cuenta")
    else:print("Usted no cuenta con los recursos necesarios para abrir una cuenta")
else:
    print("Usted debe ser mayor de edad para abrir una cuenta")