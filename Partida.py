class Partida():
    def __init__(self, palabra, intentos, tipo_palabra, nombre_jugador, palabra_aciertos=None):
        
        if(palabra == ""):
            raise ValueError("La palabra no puede estar vacia")
        if(nombre_jugador == ""):
            raise ValueError("El nombre no puede estar vacio")
        if(tipo_palabra == ""):
            raise ValueError("El tipo de palabra no puede estar vacio")
        if(intentos < 0):
            raise ValueError("Intentos no puede ser menor a 0")
        
        self._palabra = list(palabra.upper())
        self._intentos = intentos
        self._tipo_palabra = tipo_palabra.upper()
        self._nombre_jugador = nombre_jugador.upper()
        self._palabra_aciertos = [None] * len(palabra)

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, palabra):
        self._palabra = list(palabra.upper())

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, intentos):
        self._intentos = intentos

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, tipo_palabra):
        self._tipo_palabra = tipo_palabra.upper()

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, nombre_jugador):
        self._nombre_jugador = nombre_jugador.upper()

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, palabra_aciertos):
        self._palabra_aciertos = palabra_aciertos
