""""
Descripcion: A Nathan le encanta el ciclismo.

Debido a que Nathan sabe que es importante mantenerse hidratado, bebe 0.5 litros de agua por hora de ciclismo.

Te dan el tiempo en horas y necesitas devolver el número de litros que Nathan beberá, redondeado abajo.

Por ejemplo:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""
def cadena_a_flotante(cadena: str) -> float | None:
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena a convertir.
    :return: Regresa el número flotante si cumple con el formato, en caso contrario, devuelve None.
    """
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-').replace(".", "")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None






def menu_principal ():
    print("\nEste es el programa que calcula cuantos litros de agua se toma en un determinado tiempo")
    tiempo = input("Ingresa cuantas horas se ha recorrido: ")
    while not cadena_a_flotante(tiempo):
        tiempo = input("Error, intenta denuevo: ")



    print(f"Los litros tomados son {tiempo * 0.5}")

if __name__ == '__main__':
    menu_principal()