Proceso trapecio
	Definir area, largo1, largo2, altura Como Real
	Escribir "ingrese el valor del uno de los largos"
	Leer largo1
	Escribir "ingrese el valor del segundo de los largos"
	Leer largo2
	Mientras largo1=largo2 Hacer
		Escribir "los largos no pueden ser iguales, ingrese el segundo valor nuevamente"
		Leer largo2
	FinMientras
	Escribir "ingrese la altura"
	Leer altura
	area=((largo1+largo2)/2)*altura
	Escribir "el area total es de " area
	
FinProceso
