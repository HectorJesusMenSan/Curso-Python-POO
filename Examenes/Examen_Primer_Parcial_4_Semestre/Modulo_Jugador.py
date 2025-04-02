"""
Héctor Jesús Méndez Santiago.
Descripción: Modulo donde se crea la clase de
             jugadores.
"""


class Jugador :
    def __init__(self, nombre: str, numero: int, goles: int = 0):
        """
        Constructor de clase, recibe parámetros que deben ser
        asegurados.
        @param nombre: Un nombre de jugador
        @param numero: Su número correspondiente
        @param goles: Sus goles anotados
        """
        self._nombre = nombre
        self._numero = numero
        self._goles = goles
    def anotar_goles (self, no_goles: int)->None:
        """
        Métod0 para actualizar número de goles.
        @param no_goles:
        @return: Sin retornos
        """
        self._goles += no_goles
    def __str__(self)->str:
        """
        Métod0 magico para imprimir atributos y métodos de la clase.
        @return: Cadena de Texto.
        """
        return f"|Nombre_De_Jugador: {self._nombre} | Número: {self._numero} | Goles: {self._goles}| "
    #______________________________________________________MÉTODOS GETTER SETTER______________________________________________________________________

    @property
    def nombre (self)->str:
        return self._nombre
    @nombre.setter
    def nombre (self, nvo_nombre: str)->None:
        self._nombre = nvo_nombre


    @property
    def numero (self)->int:
        return self._numero
    @numero.setter
    def numero (self, nvo_numero: int)->None:
        self._numero = nvo_numero


    @property
    def goles (self)->int:
        return self._goles
    @numero.setter
    def numero (self, nvos_goles: int)->None:
        self._goles = nvos_goles

"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%MODULO%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""

if __name__ == '__main__':
    addi = Jugador("Adicto", 7)
    print(addi)
    addi.anotar_goles(3)
    print(addi)