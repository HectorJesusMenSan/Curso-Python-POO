"""24 de marzo.
    Hector Jesus Mendez Santiago
    Programacion orientada a objetos: Primer modulo, Window
"""

from Clases_Y_objetos.Ej2_Scoreboard import Scoreboard

class Window:
    def __init__(self, text:str, width:int, height:int, scoreboard:Scoreboard=Scoreboard()):
        self._title = text
        self._width = width
        self._height = height
        self._scoreboard = scoreboard
    def draw_scoreboard(self)->None:
        self._scoreboard.draw()
    def update_score(self, points:int)->None:
        self._scoreboard.puntos = points
    def __str__(self)->str:
        return f"titulo: {self._title}, width: {self._width}, heigth:{self._height}, scoreboard: {self._scoreboard}"

    @property
    def texto(self):
        return self._text
    @texto.setter
    def texto(self, text):
        self._text = text

    @property
    def widthh(self):
        return self._width
    @widthh.setter
    def widthh(self, width):
        self._width = width

    @property
    def heighter(self):
        return self._height
    @heighter.setter
    def heighter(self, height):
        self._height = height

    @property
    def tabladepuntos(self)->Scoreboard:
        return self._scoreboard
    @tabladepuntos.setter
    def tabladepuntos(self, scoreboard):
        self._scoreboard = scoreboard


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)
    buscaminas.draw_scoreboard()


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)
    solitario.draw_scoreboard()




    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas= {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas._scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")