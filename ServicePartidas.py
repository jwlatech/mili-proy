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
            #Usamos el metodo get_letras_position para encontrar todas las posiciones
            #en la que encontramos la letra elegida.
            posiciones_encontradas = self.get_letras_position(
                partida.palabra, letra)
            #Iteramos el array que contiene todas las posiciones encontradas
            #para poder meter en esas posiciones la letra elegida.
            for posicion_de_letra in posiciones_encontradas:
                partida.palabra_aciertos[posicion_de_letra] = letra
        if (partida.intentos <= 0 and partida.palabra_aciertos != partida.palabra):
            return "Perdio"
        elif(partida.palabra_aciertos == partida.palabra):
            return "Gano"
        else:
            return "Continua"

    def get_letras_position(self, palabra, letra):
        array_de_posiciones = []
        i = 0
        for letrita in palabra:
            if(letrita == letra):
                array_de_posiciones.append(i)
            i = i + 1
        return array_de_posiciones
