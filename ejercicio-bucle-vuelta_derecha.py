#coding: utf8
#David Ortega Garcia
#15/03/2018

# Inicializaciones
salir = "N"
contador=1

while ( salir=="N" ):
	  # Hago cosas
	  if ((contador==1) or(contador==2)):
        print ("Arriba")
    if ((contador==3) or(contador==4)):
        print ("Derecha")
    if ((contador==5) or(contador==6)):
        print ("Abajo")
    if ((contador==7) or(contador==8)):
        print ("Izquierda")
	  # Incremento
	  contador=contador+1
	  # Activo indicador de salida si toca
	  if (contador>8): # Condición de salida
    	    salir = "S"
