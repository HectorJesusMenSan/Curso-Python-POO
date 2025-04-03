"""
Héctor Jesús Méndez Santiago.
Descripción: Módulo donde se crea la clase de
             Torneo.
"""
from Examenes.Examen_Primer_Parcial_4_Semestre.Modulo_Equios import Equipo


class Torneo:
    def __init__(self, nombre: str, *equipos: Equipo):
        self._nombre = nombre
        self._equipos = list(equipos)

    def agregar_equipos (self, *equipos: Equipo)->None:
        for equipo in equipos:
            self._equipos.append(equipo)

    def remover_equipos (self, *equipo: Equipo )->None:
        for nombre_de_equipo in equipo:
            self._equipos.remove(nombre_de_equipo)
    def mostrar_equipos (self)->None:
        contador = 1
        print(":::E-Q-I-P-O-S:::\n")
        for equipo in self._equipos:
            print(f"{contador}. {equipo}")
            contador += 1
    def generar_rol(self)->None:
        """
        Metodo que genera un rol de equipos emparejando todos contra tods sin repetir
        @return:
        """
        if len(self._equipos) < 2:
            print("No existen eqipos suficientes.")
            return

        jornadas = []
        equipos = self._equipos.copy()

        num_jornadas = len(equipos) - 1
        for i in range(num_jornadas):
            partidos = []

            for j in range(len(equipos) // 2):
                partidos.append((equipos[j], equipos[-(j + 1)]))
            jornadas.append(partidos)
            equipos.insert(1, equipos.pop())  # Rotar equipos

        # Mostrar jornadas
        for i, jornada in enumerate(jornadas, start=1):
            print(f"Jornada {i}:")
            for partido in jornada:
                print(f" - {partido[0]} vs {partido[1]}")
            print()

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre (self, nvo_nombre):
        self._nombre = nvo_nombre

    @property
    def equipos(self):
        return self._equipos
    @equipos.setter
    def equipos(self, nvs_equipos):
        self._equipos = nvs_equipos