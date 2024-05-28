divisas = {'Euro': '€', 'Dolar': '$', 'Yen': '¥'}

divisa = input("Ingrese una divisa: ")

if divisa in divisas:
    simbolo = divisas[divisa]
    print("El símbolo de", divisa, "es", simbolo)
else:
    print("La divisa ingresada no está en el diccionario.")