Proceso promedionotas
	definir A, B, C, D como real
	Escribir "escriba la primera nota"
	Leer A
	Escribir "escriba la segunda nota"
	Leer B
	Escribir "escriba la tercera nota"
	Leer C
	Si (A>7.0 o A<1.0) o (B>7.0 o B<1.0) o (C>7.0 o C<1.0) Entonces
		Escribir "ponte vio esas no son tus notas"
	SiNo
		D = (A+B+C)/3
		Si D>=4.0 Entonces
			Escribir "aprobaste papi"
		SiNo
			Escribir "poco vio, reprobaste"
		FinSi
	FinSi
FinProceso
