edad= int(input("Ingrese su edad: "))
if edad < 4:
    print("Su entrada es gratis")
else:
    if edad < 18:
        print("Su entrada cuesta $5.000")
    else:
        if edad >= 18:
            print("Su entrada cuesta $10.000")