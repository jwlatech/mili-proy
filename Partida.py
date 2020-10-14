class Partida():
    def __init__(self, palabra, tipo_palabra, intentos, nombre_jugador, palabra_aciertos):
        self._palabra = palabra
        self._tipo_palabra = tipo_palabra
        self._intentos = intentos
        self._nombre_jugador = nombre_jugador
        self._palabra_aciertos = palabra_aciertos

    @property
    def palabra(self):
        return self._palabra

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @property
    def intentos(self):
        return self._intentos

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos
