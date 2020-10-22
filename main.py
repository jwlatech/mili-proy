""" from palabraService import PalabraService
from Persona import Persona
from Palabra import Palabra
from AhorcadoService import AhorcadoService


class Menu():
    def seleccion_jugadores(self):
        print("Seleccione jugadores")
        print("1 jugador")
        print("2 jugadores")
        return int(input("Seleccione opcion => "))


if __name__ == "__main__":

    while True:
        cant_jugadores = Menu().seleccion_jugadores()
        if cant_jugadores == 1:
            nombre = input("Ingrese su nombre")
            persona = Persona(nombre)
            palabra = PalabraService().get_random_palabra()
            dificultad = int(input("Seleccione grado de dificultad"))
            AhorcadoService().start_game(palabra, dificultad, persona)
        else:
            print("Jugador 1 : Ingrese su nombre")
            nombreJug1 = input("Nombre => ")
            jugador1 = Persona(nombreJug1)
            print("Jugador 2 : Ingrese su nombre")
            nombre_jug_2 = input("Nombre => ")
            jugador2 = Persona(nombre_jug_2)

            quiere_seguir = True

            while quiere_seguir:
                print(jugador1.nombre, " : Ingrese un tipo de palabra")
                tipo_de_palabra = input("Tipo de palabra => ")
                print(jugador1.nombre, " : Ingrese una palabra")
                palabra = input("Palabra => ")
                palabra = Palabra(tipo_de_palabra, palabra)
                print(jugador2.nombre, " : Ingrese la dificultad")
                dificultad = input("Dificultad => ")
                AhorcadoService().start_game(palabra, dificultad, jugador1, jugador2)
                print(jugador2.nombre, " : Ingrese un tipo de palabra")
                tipo_de_palabra = input("Tipo de palabra => ")
                print(jugador2.nombre, " : Ingrese una palabra")
                palabra = input("Palabra => ")
                palabra = Palabra(tipo_de_palabra, palabra)
                print(jugador1.nombre, " : Ingrese la dificultad")
                dificultad = input("Dificultad => ")
                AhorcadoService().start_game(palabra, dificultad, jugador2, jugador1)
                eligio_mal = True
                while eligio_mal:
                    print("QUIERE SEGUIR VICIANDO?")
                    print("1. SI")
                    print("2. NO")
                    seleccion = int(input("Elija una opcion"))
                    if not isinstance(seleccion, int):
                        quiere_seguir = False
                        break
                    elif seleccion == 2:
                        quiere_seguir = False
                        eligio_mal = False
                    elif seleccion == 1:
                        quiere_seguir = True
                        eligio_mal = False
                    else:
                        print(
                            "No eligio una opcion correcta, porfavor elija otra vez")
 """