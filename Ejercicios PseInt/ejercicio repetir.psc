Proceso sin_titulo
	Definir clave Como Caracter
	Repetir
		Escribir "ingrese su clave de acceso: "
		leer clave
		Si clave <> "1234" Entonces
			Escribir "clave incorrecta, ingrese nuevamente"
		FinSi
	Hasta Que clave = "1234"
	Escribir "bienvenido"
FinProceso
