Proceso sin_titulo
	Definir x Como Caracter
	//x sera el operador
	Definir A, B Como Real
	//variables
	Definir C Como Real
	//resultado
	Escribir "que desea hacer (sumar/restar/multiplicar/dividir)"
	Leer  x
	si x="sumar" Entonces
		
			Escribir "introduzca su primer numero"
			leer A
			Escribir "introduzca su segundo numero"
			leer B
			C=A+B
			Escribir "la suma total es " C
		SiNo
			si x="restar" Entonces
				Escribir "introduzca su primer numero"
				leer A
				Escribir "introduzca su segundo numero"
				leer B
				C=A-B
				Escribir "la resta total es de " C
			SiNo
				si x= "multiplicar" Entonces
					Escribir "introduzca su primer numero"
					leer A
					Escribir "introduzca su segundo numero"
					leer B
					C=A*B
					Escribir "la multiplicacion total es de " C
				SiNo
					si x="dividir" Entonces
						Escribir "introduzca su primer numero"
						leer A
						Escribir "introduzca su segundo numero"
						leer B
						C=A/B
						Escribir "la division total es de " C
					FinSi
				FinSi
			FinSi
		FinSi
		//dependiendo de la operacion seleccionada hara una u otra operacion
FinProceso
