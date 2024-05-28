inversion= int(input("Ingrese la cantidad de dinero que desea invertir: "))
interes=float(input("Ingrese el porcentaje de interés anual: "))

capital=inversion + (inversion*interes)

print("Su capital después de un año será de " ,round(capital,2))