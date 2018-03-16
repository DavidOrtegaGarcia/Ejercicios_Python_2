#coding: utf8
#David Ortega Garcia
#15/03/2018

# Inicializaciones
salir = "N"
contador=1

while ( salir=="N" ):
	  # Hago cosas
    if ((contador % 8 == 1) or(contador %8 == 2)):
        print ('Arriba')
    if ((contador % 8 == 3) or(contador %8 == 4)):
        print ('Derecha')
    if ((contador % 8 == 5) or(contador %8 == 6)):
        print ('Abajo')
    if ((contador %8 == 7) or(contador %8 == 0)):
        print ('Izquierda')
    # Incremento
    contador=contador+1
    # Activo indicador de salida si toca
    if (contador>8): # Condición de salida
        salir = "S"
