from Ahorcado import Ahorcado
from AhorcadoService import AhorcadoService

class Menu():
    def seleccion_jugadores(self):
        print("Seleccione Opcion")
        print("1 => 1 jugador")
        print("2 => 2jugadores")
        print("3 => Ver resultados")
        return int(input("Seleccione opcion => "))


if __name__ == "__main__":

    while True:
        cant_jugadores = Menu().seleccion_jugadores()
        if cant_jugadores == 1:
            result = Ahorcado().un_jugador()
        elif cant_jugadores == 2:
            result = Ahorcado().dos_jugadores()
        else:
            AhorcadoService().ver_partida_guardada()
