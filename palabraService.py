import random
from Repository import Repositorios
from Palabra import Palabra


class PalabraService():
    def get_random_palabra(self):
        palabra = random.choice(Repositorios.palabrasList)
        return palabra
