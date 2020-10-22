class Palabra():
    def __init__(self, tipoPalabra="", palabra=""):
        self._palabra = palabra
        self._tipoPalabra = tipoPalabra

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, palabra):
        self._palabra = palabra

    @property
    def tipoPalabra(self):
        return self._tipoPalabra

    @tipoPalabra.setter
    def tipoPalabra(self, tipoPalabra):
        self._tipoPalabra = tipoPalabra
