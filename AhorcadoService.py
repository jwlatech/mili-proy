from Repository import Repositorios
from Partida import Partida


class AhorcadoService():
    
    def guardar_partida(self, partida, key):
        Repositorios().partida[key] = partida.__dict__

    def ver_partida_guardada(self):
        print(Repositorios().partida)