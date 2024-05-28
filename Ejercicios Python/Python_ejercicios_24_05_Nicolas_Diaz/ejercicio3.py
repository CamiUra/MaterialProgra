peso=float(input("Introduzca su peso en kilos: "))
altura=float(input("Introduzca su altura en metros: "))
imc= peso/altura**2
print("Su IMC es de " ,round(imc, 2))