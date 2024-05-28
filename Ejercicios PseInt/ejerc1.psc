Proceso sin_titulo
	definir A, B, C como entero
	Escribir "inserte valor1:"
	Leer A
	Escribir "inserte valor2:"
	Leer B
	Escribir "inserte valor3:"
	Leer C
	Si A>B Entonces
		Si A>C Entonces
			Escribir A "es el mayor"
		SiNo
			Escribir C "es el mayor"
		FinSi
	SiNo
		Si B>C Entonces
			Escribir B "es el mayor"
		SiNo
			Escribir C "es el mayor"
		FinSi
	FinSi
FinProceso
