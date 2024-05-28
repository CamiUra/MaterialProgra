key = "contraseña"
password= str(input("Ingrese su contraseña: "))
if key == password.lower():
    print("Clave válida")
else:
    print("Clave inválida")