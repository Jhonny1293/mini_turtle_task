posicion_x = 0

def mover_derecha(pasos):
    global posicion_x
    print(" " * posicion_x + "-" * pasos + "|")
    posicion_x += pasos

def mover_abajo(pasos):
    global posicion_x
    for _ in range(pasos - 1):
        print(" " * posicion_x + "|")

def reiniciar():
    global posicion_x
    posicion_x = 0
