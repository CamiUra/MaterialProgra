Proceso ejercicio1
	definir n1, n2, n3, n4, n5, n6 Como Real
	definir nf Como Real
	Escribir "ingrese su primera nota"
	Leer n1
	Mientras  n1>7.0 o n1<1.0 Hacer
		Escribir "valor invalido, ingrese su nota nuevamente"
		Leer n1
	FinMientras	
	Escribir "ingrese su segunda nota"
	leer n2
	Mientras n2>7.0 o n2<1.0 Hacer
		Escribir "valor invalido, ingrese su nota nuevamente"
		Leer n2
	FinMientras
	Escribir "ingrese su tercera nota"
	Leer n3
	Mientras n3>7.0 o n3<1.0 Hacer
		Escribir "valor invalido, ingrese su nota nuevamente"
		Leer n3
	FinMientras
	Escribir "ingrese su cuarta nota"
	Leer n4
	Mientras n4>7.0 o n4<1.0 Hacer
		Escribir "valor invalido, ingrese su nota nuevamente"
		leer n4
	FinMientras
	Escribir "ingrese su quinta nota"
	Leer n5
	Mientras n5>7.0 o n5<1.0 Hacer
		Escribir "valor invalido, ingrese su nota nuevamente"
		Leer n5
	FinMientras
	Escribir "ingrese su sexta nota"
	Leer n6
	Mientras n6>7.0 o n6<1.0 Hacer
		Escribir "valor invalido, ingrese su nota nuevamente"
		Leer n6
	FinMientras
	nf = (n1+n2+n3+n4+n5+n6)/6
	Escribir "su promedio final es " nf
	
FinProceso
