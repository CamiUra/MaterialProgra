Proceso sin_titulo
	// crear un programa que pida al usuario una contraseņa de forma repetitiva mientras que no intruduzca "1234". Y cuando introduzca la contraseņa correcta
	//escribir "bienvenido" como comando
	Definir clave Como Caracter
	Escribir "ingrese su clave"
	leer clave
	Mientras clave <> "1234" Hacer
		Escribir "clave incorrecta, ingrese nuevamente"
		Leer clave
	FinMientras
	Escribir "bienvenido"

FinProceso
