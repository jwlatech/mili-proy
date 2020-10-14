from Repository import Repositorios
from Partida import Partida
from Persona import Persona


class AhorcadoService():
    def start_game(self, palabra, grado_dificultad, jugador, jugador2=False):
        palabra_incompleta = "_" * len(palabra.palabra)
        adivinada = False
        letras_intentos = []
        intentos = len(palabra.palabra)*int(grado_dificultad)
        intentos_realizados = 0
        print("Hora de empezar a jugar!!! \n\n")
        print(palabra.tipoPalabra, "\n\n")
        print(palabra_incompleta)
        print("\n\n\n")
        while not adivinada and intentos > 0:
            print("Te quedan ", intentos, " intentos")
            intento = input("Adivina una letra! => ")
            intentos_realizados = intentos_realizados + 1
            if intento in letras_intentos:
                print("Ya intentaste de adivinar la letra ",
                      intento, " :( \n\n")
            elif intento not in palabra.palabra:
                print("Intento fallido! Vuelve a intentarlo\n\n")
                intentos = intentos - 1
                letras_intentos.append(intento)
            else:
                print("Epaaaa esa letra si esta en la palabra rey! \n\n")
                letras_intentos.append(intento)
                palabra_como_lista = list(palabra_incompleta)
                indices = [i for i, letter in enumerate(
                    palabra.palabra) if letter == intento]
                for index in indices:
                    palabra_como_lista[index] = intento
                palabra_incompleta = "".join(palabra_como_lista)
                if "_" not in palabra_incompleta:
                    adivinada = True
            print(palabra_incompleta)
            print("\n\n")
        if adivinada:
            print("Ganaste master!!")
        else:
            print("Te quedaste sin intentos!!! </3. La palabra era ",
                  palabra.palabra)
        if not jugador2:
            self.guardar_partida(palabra, jugador.nombre,
                                 intentos_realizados, palabra_incompleta, intentos)
        else:
            self.guardar_partida(palabra, jugador.nombre,
                                 intentos_realizados, palabra_incompleta, intentos, jugador2.nombre)
        print("\n\n\n\n\n ", self.ver_partida_guardada())

    def guardar_partida(self, palabra, jugador, intentos, aciertos, intentos_restantes, jugador2=False):
        if not jugador2:
            partida = Partida(list(palabra.palabra), palabra.tipoPalabra,
                              intentos,  jugador, list(aciertos))
            Repositorios.partida["COMPUTADORA"] = partida.__dict__
        else:
            partida = Partida(list(palabra.palabra), palabra.tipoPalabra,
                              intentos,  jugador2, list(aciertos))
            Repositorios.partida[jugador] = partida.__dict__

    def ver_partida_guardada(self):
        return Repositorios.partida
