Proceso sin_titulo
	Definir x Como Entero
	//x es el numero que elegira el usuario
	Escribir "introduzca un numero"
	leer x
	si x>10 Entonces
		//condiciono que el numero no pueda ser mayor a 10
		Escribir "el numero maximo es 10, intente nuevamente"
		leer x
	FinSi
	Para x=x hasta 10 con paso 1 Hacer
		Escribir x
		//muestra los numeros desde el que escogio hasta el 10
	FinPara
FinProceso
