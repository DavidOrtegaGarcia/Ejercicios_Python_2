#coding: utf8
#David Ortega Garcia
#14/03/2018

# Inicializaciones
salir = "N"
numero=1
resultado=0
while ( salir=="N" ):
	# Hago cosas
    if (numero%2==0):
    print numero
    if (numero%2==0):
        print "+"
    
	# Incremento
	numero=numero+1
	if (numero%2==0):
        resultado=resultado+`numero 
	# Activo indicador de salida si toca
	if ( numero>=4 ): # Condición de salida
    	    salir = "S"
          print "=",resultado
