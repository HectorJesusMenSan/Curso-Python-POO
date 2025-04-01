"""24 de marzo.
    Hector Jesus Mendez Santiago
    Programacion orientada a objetos: Primer modulo, Scoreboard
"""

class Scoreboard:

    def __init__(self, points:int=0, text_color:tuple[int]=(0, 0, 0), font:str = "kilmono", size:float=48 ):
        """
        Constructor de atributos de la clase.
        @param points: Recibe puntos de un usuario
        @param text_color: Recibe datos del color de texto en tuplas
        @param font: Es un string
        @param size: Recibe un dato flotante que determina un tamaño
        """
        self._points = points
        self._text_color = text_color
        self._font = font
        self._size = size
    def __str__(self)->str:
        """
        Métod0 magico para mostrar escrituras en pantalla.
        Le puse 0 porque marca un T0D0
        @return: Retorna un mensaje o un str
        """
        return f"Puntos: {self._points}, Texto: {self._text_color}, font: {self._font}, size: {self._size} "
    def draw (self):
        """
        Metodo para mostrar puntos
        @return: Sin retornos
        """
        print(self._points)


    @property
    def puntos (self)->int:
        return self._points
    @puntos.setter
    def puntos (self, points):
        self._points = points

    @property
    def texto_color(self) -> tuple :
        return self._text_color
    @texto_color.setter
    def texto_color(self, text_color):
        self._text_color = text_color

    @property
    def fonter(self) -> str:
        return self._font
    @fonter.setter
    def fonter(self, font):
        self._font = font

    @property
    def sizee(self) -> float:
        return self._size
    @sizee.setter
    def sizee(self, size):
        self._size = size




""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(10, font="Arial", text_color=(127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()