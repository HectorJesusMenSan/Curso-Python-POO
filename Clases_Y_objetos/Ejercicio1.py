"""
-Nombre:---------Hector Jesus Mendez Santiago.
-Descripcion:----Un programa que genera un objeto
                 de un personaje que se mueve en
                 una ventana con un cierto límite.
-Fecha:----------12-de-marzo-de-2025.
"""
from typing import Tuple


def solicitud_de_datos ()->str:
    opcion = input("Ingrese ordenes de movimiento o presione S para salir: ")
    while not opcion.isalpha():
        opcion=input("Dato invalido, intentalo de nuevo: ")
    opcion = opcion.lower()
    return opcion



def movimientos_en_ventana(ordenes:str, x:int, y:int)->Tuple[int,int]:
    """
    Funcion que impementa los movimientos respectivos, tomando en cuenta el límite de 10
    :param ordenes: Direccion de movimiento
    :return: Sin retornos
    """

    coordenada_x, coordenada_y = x, y
    palabras_validas = ["a","r","i","d"]
    for palabra in list(ordenes):
        if palabra  not in palabras_validas:
            print("Error")
        else:

            if palabra == "a":
                if coordenada_y >= 0 and coordenada_y <10:
                    coordenada_y += 1
            elif palabra== "r":
                if coordenada_y>0 and coordenada_y<=10:
                    coordenada_y -= 1
            elif palabra == "d":
                if coordenada_x>=0 and coordenada_x<10:
                    coordenada_x += 1
            elif palabra == "i":
                if coordenada_x>0 and coordenada_x<10:
                    coordenada_x -= 1

    return coordenada_x, coordenada_y








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
        self.ordenes = ordenes


        self.x, self.y = movimientos_en_ventana(self.ordenes, self.x, self.y)





    def poscion_de_personaje (self)->None:
        """
        Metodo de la posicion actual del personaje
        :return: Sin retornos

        """
        posiciones = (self.x, self.y)

        print(posiciones)

    def __str__(self)->str:
        return f"PERSONAJE (id de personaje: {self.id}, x: {self.x}, y:{self.y}.)"


if __name__ == '__main__':
    personaje_mesant = Personaje()
    print(personaje_mesant)

    ordenes = None

    while ordenes!="s":
        ordenes=solicitud_de_datos()
        if ordenes != "s":
           personaje_mesant.mover_personaje(ordenes)
           print(personaje_mesant)
        else:
            print("Programa finalizado")

