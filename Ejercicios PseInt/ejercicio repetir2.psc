Proceso sin_titulo
	//crear un programa que pida al usuario un c�digo de usuario y una contrase�a, debe repetirse hasta que el c�digo sea "1" y la contrase�a sea "1234"
	Repetir
		Escribir "ingrese su usuario"
		leer id
		Escribir "ingrese su clave"
		leer clave
		si id <> 1 o clave <> 1234 Entonces
			Escribir "usuario o clave incorrecta, intente nuevamente"
		FinSi
	Hasta Que id = 1 Y clave = 1234
	Escribir "bienvenido"
FinProceso
