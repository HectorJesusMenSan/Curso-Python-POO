"""
Héctor Jesús Méndez Santiago.
Descripción: Módulo para la clase de equipos
"""
from Examenes.Examen_Primer_Parcial_4_Semestre.Modulo_Jugador import Jugador


class Equipo:
    no_id = 1
    def __init__(self, nombre: str, *jugadores: Jugador):
        self._nombre = nombre
        self._jugadores = list (jugadores)
        self._id_equipo = Equipo.no_id
        Equipo.no_id += 1

    def agregar_jugadores (self, *jugadores:Jugador)->None:
        for jugador in jugadores:
            self._jugadores.append(jugador)

    def remover_jugadores (self, *jugadores:Jugador)->None:
        for jugador in jugadores:
            self._jugadores.remove(jugador)

    def mostrar_jugadores (self)->None:
        contador = 1
        for jugador in self._jugadores:
            print(f"jugador {contador}: {jugador.nombre}\n")
            contador += 1

    def total_de_goles (self)->int:

        contador_de_goles = 0
        for jugador in self._jugadores:
            contador_de_goles += jugador.goles
        return contador_de_goles

    def __str__(self)->str:
        jugadores = ", ".join(str(jugador) for jugador in self._jugadores)
        return f"Equipo: {self._nombre}, id={self._id_equipo}, jugadores: {jugadores}"

#______________________Encapsulamiento___________________________________________________________________________________________


    @property
    def nombre (self)->str:
        return self._nombre
    @nombre.setter
    def nombre (self, nvo_nombre: str)->None:
        self._nombre = nvo_nombre

    @property
    def jugadores (self)->list:
        return self._jugadores
    @jugadores.setter
    def jugadores (self, nvos_jugadores: list)->None:
        self._jugadores = nvos_jugadores

    @property
    def id_equipo (self)->int:
        return self._id_equipo
    @id_equipo.setter
    def id_equipo (self, nvo_id):
        self._id_equipo = nvo_id

"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""
if __name__ == '__main__':
    addi = Jugador("addi", 4, 2)
    alberto = Jugador("alberto", 2, 0)
    unsij = Equipo("unsij", alberto, addi)
    print(unsij)
    juan = Jugador("JUAM", 3, 1)
    unsij.agregar_jugadores(juan)
    print(unsij)
    unsij.remover_jugadores(addi, alberto)
    print(unsij)
    unsij.agregar_jugadores(addi, alberto)
    unsij.mostrar_jugadores()
    print(unsij.total_de_goles())
    alberto.anotar_goles(6)
    print(unsij.total_de_goles())