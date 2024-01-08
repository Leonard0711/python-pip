import random

def opciones_eleccion():
    opciones = ("piedra", "papel", "tijera")
    eleccion_jugador = input("piedra, papel o tijera => ").lower()

    if not eleccion_jugador in opciones:
        print("Opción no valida, revisa bien!!!")

        return None, None
    
    eleccion_machine = random.choice(opciones)
    print("Elección del jugador => ", eleccion_jugador)
    print("Elección de la máquina => ", eleccion_machine)

    return eleccion_jugador, eleccion_machine

def reglas_juego(eleccion_jugador, eleccion_machine, ganadas_jugador, ganadas_machine):
    if eleccion_jugador == eleccion_machine:
        print("Empate!!!")

    elif eleccion_jugador == "tijera":
        if eleccion_machine == "papel":
            print("Tijera gana a papel")
            print("Jugador gana")
            ganadas_jugador += 1
        else:
            print("Piedra gana a tijera")
            print("Máquina gana")
            ganadas_machine += 1

    elif eleccion_jugador == "piedra":
        if eleccion_machine == "tijera":
            print("Piedra gana a tijera")
            print("Jugador gana")
            ganadas_jugador += 1
        else:
            print("Papel gana a piedra")
            print("Máquina gana")
            ganadas_machine += 1

    elif eleccion_jugador == "papel":
        if eleccion_machine == "piedra":
            print("Papel gana a piedra")
            print("Jugador gana")
            ganadas_jugador += 1
        else:
            print("Tijera gana a papel")
            print("Máquina gana")
            ganadas_machine += 1

    return ganadas_jugador, ganadas_machine

def juego():
    ganadas_jugador = 0
    ganadas_machine = 0
    rondas = 1

    while True:
        print("*" * 10)
        print("Rondas", rondas)
        print("*" * 10)

        print("Ganadas por el jugador", ganadas_jugador)
        print("Ganadas por machine", ganadas_machine)
        rondas += 1


        eleccion_jugador, eleccion_machine = opciones_eleccion()
        ganadas_jugador, ganadas_machine = reglas_juego(eleccion_jugador, eleccion_machine, ganadas_jugador, ganadas_machine)
        
        if ganadas_machine == 2:
            print("Machine gana la partida")
            break
        
        if ganadas_jugador == 2:
            print("Jugador ganó la partida")
            break

juego()