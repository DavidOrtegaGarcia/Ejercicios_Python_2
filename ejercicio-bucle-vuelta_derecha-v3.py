# coding: utf8
# Inicializaciones
salir = "N"
vueltas=1
direccion= raw_input ("Quiere girar hacia la izquierda(I) o hacia la derecha(D):")
turnos= input ("Cuantos turnos quieres hacer? ")
maximo=8*turnos


while ( salir=="N" ):
    # Hago cosas
    if (direccion == 'D'):
        if ((vueltas % 8 == 1) or(vueltas % 8 == 2)):
            print ("Arriba")
        if ((vueltas % 8 == 3) or(vueltas % 8 == 4)):
            print ('Derecha')
        if ((vueltas % 8 == 5) or(vueltas % 8 == 6)):
            print ('Abajo')
        if ((vueltas % 8 == 7) or(vueltas % 8 == 0)):
            print ('Izquierda')
    else:
        if ((vueltas % 8 == 1) or(vueltas % 8 == 2)):
            print ('Arriba')
        if ((vueltas % 8 == 3) or(vueltas % 8 == 4)):
            print ('Izquierda')
        if ((vueltas % 8 == 5) or(vueltas % 8 == 6)):
            print ('Abajo')
        if ((vueltas % 8 == 7) or(vueltas % 8 == 0)):
            print ('Derecha')
    # Incremento
    vueltas=vueltas+1
    # Activo indicador de salida si toca
    if ( vueltas>maximo ): # Condición de salida
            salir = "S"
