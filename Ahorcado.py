from ServicePartidas import ServicesPartidas


class Ahorcado():
    def un_jugador(self):
        nombre = input("Ingrese su nombre => ")
        print("Nombre elegido", nombre)
        dificultad = input("Ingrese la dificultad del 1 al 10 => ")
        print("Dificultad elegida", dificultad)
        partida = ServicesPartidas().iniciar_partida(nombre, dificultad, "", "")
        termino = False
        while not termino:
            letra = input("Ingrese una letra => ")
            if(letra == "salir"):
                print("Gracias por jugar!")
                return True
            print("Letra elegida", letra)
            result = ServicesPartidas().intentar_letra(partida, letra)
            print(partida.intentos)
            print(partida.palabra_aciertos)
            if(result != "Continua"):
                return True

    def dos_jugadores(self):
        nombre = input("Jugador 1 ingrese su nombre => ")
        print("Nombre Jugador 1", nombre)
        dificultad = input("Ingrese la dificultad del 1 al 10 => ")
        print("Dificultad elegida", dificultad)
        palabra = input("Ingrese la palabra para el jugador 2 => ")
        tipo_palabra = input("Ingrese el tipo de palabra")
        partida = ServicesPartidas().iniciar_partida(nombre, dificultad, palabra, tipo_palabra)
        termino = False
        while not termino:
            letra = input("Ingrese una letra => ")
            if(letra == "salir"):
                print("Gracias por jugar!")
                return True
            print("Letra elegida", letra)
            result = ServicesPartidas().intentar_letra(partida, letra)
            print(partida.intentos)
            print(partida.palabra_aciertos)
            if(result != "Continua"):
                termino = True
            nombre = input("Jugador 1 ingrese su nombre => ")
        print("Nombre Jugador 1", nombre)
        dificultad = input("Ingrese la dificultad del 1 al 10 => ")
        print("Dificultad elegida", dificultad)
        palabra = input("Ingrese la palabra para el jugador 2 => ")
        tipo_palabra = input("Ingrese el tipo de palabra")
        partida = ServicesPartidas().iniciar_partida(nombre, dificultad, palabra, tipo_palabra)
        termino = False
        while not termino:
            letra = input("Ingrese una letra => ")
            if(letra == "salir"):
                print("Gracias por jugar!")
                return True
            print("Letra elegida", letra)
            result = ServicesPartidas().intentar_letra(partida, letra)
            print(partida.intentos)
            print(partida.palabra_aciertos)
            if(result != "Continua"):
                termino = True
