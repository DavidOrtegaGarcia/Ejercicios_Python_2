#coding: utf8
#David Ortega Garcia
#11/03/2018

# Inicializaciones
salir = "N"
numero=1
resultado=0
while ( salir=="N" ):
	# Hago cosas
	print (numero)

	# Incremento
	numero=numero+1
	resultado=resultado+numero
	# Activo indicador de salida si toca
	if (resultado>=15): # Condición de salida
    	    salir = "S"
print (resultado)
