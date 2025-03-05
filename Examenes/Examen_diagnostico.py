"""Descripción del programa:

El curso tiene los siguientes equipos:

Los Algoritmos Anarquistas: Héctor, Addi y Jesús Alberto.
Los Hackers de Café: Tania, Patricia, Rebeca.
Los Codificadores nocturnos: Jamileth, Bryan, Rosalinda.
Los Ctrl+Z: Galilea, Jennifer, Juan.


Este programa debe generar 6 nuevos equipos de 2 personas cada uno, pero con la restricción de que no puede haber dos personas que ya estuvieron en el mismo equipo de arriba ☝️. """
from random import random, randint
import random


def imprimir_equipos (algoritmos_anarquistas:list, hackers_cafe:list, codificadores_nocturnos:list, controlz:list ) -> None:
    contador = 0
    print("\nEl equipo Algoritmos Anarquistas: ")
    for alumno in algoritmos_anarquistas:
        contador+=1
        if len(algoritmos_anarquistas) != contador :
            print(alumno, end=", ")
        else:
            print(alumno, end=".")
    contador = 0

    print("\nEl equipo Hackers de Café: ")
    for alumno in hackers_cafe:

        contador+=1
        if len(algoritmos_anarquistas) != contador :
            print(alumno, end=", ")
        else:
            print(alumno, end=".")
    contador = 0

    print("\nEl equipo Codificadores nocturnos: ")
    for alumno in codificadores_nocturnos:
        contador+=1
        if len(algoritmos_anarquistas) != contador :
            print(alumno, end=", ")
        else:
            print(alumno, end=".")
    contador = 0

    print("\nEl equipo Ctrl+Z: ")
    for alumno in controlz:
        contador+=1
        if len(algoritmos_anarquistas) != contador :
            print(alumno, end=", ")
        else:
            print(alumno, end=".")





def menu_Principal ()->None:
    diccionario_de_alumnos = {'Hector': 1,'Addi': 1, 'Alberto': 1, 'Tania':2,'Patricia':2, 'Rebeca':2,
                              'Jamileth':3,'Bryan':3,'Rosalinda':3, 'Galilea':4, 'Jennifer':4, 'Juan':4}
    algoritmos_anarquistas= ["Hector", "Addi", "Alberto"]
    hackers_cafe=["Tania", "Patricia", "Rebeca"]
    codificadores_nocturnos=["Jamileth", "Bryan", "Rosalinda"]
    controlz = ["Galilea", "Jennifer", "Juan"]

    imprimir_equipos(algoritmos_anarquistas, hackers_cafe, codificadores_nocturnos, controlz)
    print()
    print("\nSe asignaron nuevos equipos: \n")

    for i in range(0,6):
        alumno1 = random.choice(list (diccionario_de_alumnos.keys()))
        alumno2 = random.choice(list (diccionario_de_alumnos.keys()))

        while diccionario_de_alumnos.get(alumno1) == diccionario_de_alumnos.get(alumno2):
            alumno1 = random.choice(list(diccionario_de_alumnos.keys()))
            alumno2 = random.choice(list(diccionario_de_alumnos.keys()))


        print(f"\nEquipo {i+1}:")
        print(f"{alumno1} y {alumno2}.")

        diccionario_de_alumnos.pop(alumno1)
        diccionario_de_alumnos.pop(alumno2)





if __name__ == '__main__':
    menu_Principal()

