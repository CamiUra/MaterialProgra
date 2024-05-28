Proceso promedio
	definir A, B, C, D Como Real
	definir n1, n2, n3, n4 Como Real
	definir nf Como Real
	Escribir "ingrese su primera nota"
	leer n1
	Escribir "ingrese su segunda nota"
	leer n2
	Escribir "ingrese su tercera nota"
	leer n3
	Escribir "ingrese su cuarta nota"
	leer n4
	A=n1*0.15
	B=n2*0.2
	C=n3*0.35
	D=n4*0.3
	nf=A+B+C+D
	si nf>=3.95 Entonces
		Escribir "su nota final es de " nf " y ha aprobado"
	SiNo
		Escribir "su nota final es de " nf " y ha reprobado"
	FinSi
	
FinProceso
