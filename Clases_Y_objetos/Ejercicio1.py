"""
-Nombre:---------Hector Jesus Mendez Santiago.
-Descripcion:----Un programa que genera un objeto
                 de un personaje que se mueve en
                 una ventana con un cierto límite.
-Fecha:----------12-de-marzo-de-2025.
"""

def movimientos_en_ventana(ordenes:str)->None:
    """
    Funcion que impementa los movimientos respectivos, tomando en cuenta el límite de 10
    :param ordenes: Direccion de movimiento
    :return: Sin retornos
    """
    pass

class Personaje:
    """
    Clase: Personaje.
    Atributos: contador_id, eje y, eje x.
    Metodos: __init__, moverse(direccion_de_movimiento), posicion(), __str__.
    """
    no_id = 1
    def __init__(self):
        """
        -Atributos del objeto

        """
        #Coordenadas
        self.x = 0
        self.y = 0
        #Contador de objetos creados
        self.id = Personaje.no_id
        Personaje.no_id += 1
    #Metodos
    def mover_personaje (self, ordenes:str)->None:
        """
        Metodo para generar movimientos de un personaje o un objeto
        :param ordenes: Direccion de movimiento leidos de consola por un usuario
        :return: Sin retornos

        """
        pass
    def poscion_de_personaje (self)->None:
        """
        Metodo de la posicion actual del personaje
        :return: Sin retornos

        """
        pass
    def __str__(self)->str:
        return f"PERSONAJE (id de personaje: {self.id}, x: {self.x}, y:{self.y})"


if __name__ == '__main__':
    personaje_mesant = Personaje()
    print(personaje_mesant)

