Proceso mayormenor
	Definir A, B, C como real
	Escribir "introduzca el primer numero"
	Leer A
	Escribir "introduzca el segundo numero"
	Leer B
	Escribir "introduzca el tercer numero"
	Leer C
	Si A=B o A=C o B=C Entonces
		Escribir "los valores deben ser distintos, intente nuevamente"
	SiNo
		Si A>B y A>C Entonces
			Escribir A, " es el mayor y"
		SiNo
			Si B>A y B>C Entonces
				Escribir B, " es el mayor y"
			SiNo
				Si C>A y C>B Entonces
					Escribir C, " es el mayor y"
				FinSi
			FinSi
		FinSi
		Si A<B y A<C Entonces
			Escribir A, " es el menor"
		SiNo
			Si B<A y B<C Entonces
				Escribir B, " es el menor"
			SiNo
				Si C<A y C<B Entonces
					Escribir C, " es el menor"
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
