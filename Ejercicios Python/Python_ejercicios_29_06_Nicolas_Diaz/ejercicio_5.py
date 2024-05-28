nombre = str(input("Indique su nombre: "))
edad = int(input("Indique su edad: "))
direccion = str(input("Indique su dirección: "))
telefono = str(input("Indique su número de teléfono: "))

datos = (nombre, edad, direccion, telefono)

print(datos[0],"tiene " ,datos[1],"años, vive en" ,datos[2], "y su numero es",datos[3],)