from Partida import Partida
from Repository import Repositorios
import random


class ServicesPartidas():
    def iniciar_partida(self, nombre, dificultad, palabra, tipo_palabra):
        if(dificultad < 1 or dificultad > 10):
            raise ValueError("La dificultad debe estar entre 1 y 10")
        else:
            if(palabra == "" or tipo_palabra == ""):
                p = self.get_random_palabra()
                palabra = p.get('palabra')
                tipo_palabra = p.get('tipo_palabra')
            intentos_para_partida = dificultad * len(palabra)
            return Partida(palabra, intentos_para_partida, tipo_palabra, nombre)

    def get_random_palabra(self):
        p = random.choice(Repositorios().palabrasList)
        return {'palabra': p.palabra, 'tipo_palabra': p.tipoPalabra}

    def intentar_letra(self, partida, letra):
        partida.intentos = partida.intentos - 1
        if(partida.intentos < 0):
            raise ValueError("Se acabaron los intentos")
        if(letra in partida.palabra):
            index = self.get_letra_position(partida.palabra, letra)
            partida.palabra_aciertos[index] = letra
        if (partida.intentos <= 0 and partida.palabra_aciertos != partida.palabra):
            return "Perdio"
        elif(partida.palabra_aciertos == partida.palabra):
            return "Gano"
        else:
            return "Continua"

    def get_letra_position(self, palabra, letra):
        i = 0
        for letrita in palabra:
            if(letrita == letra):
                return i
            i = i + 1
