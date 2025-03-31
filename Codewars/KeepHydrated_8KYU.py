"""
Nombre: Héctor Jesús Méndez Santiago
Descripción: A Nathan le encanta el ciclismo.

Debido a que Nathan sabe que es importante mantenerse hidratado, bebe 0.5 litros de agua por hora de ciclismo.

Te dan el tiempo en horas y necesitas devolver el número de litros que Nathan beberá, redondeado abajo.

Por ejemplo:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""
def operaciones (tiempo_recorrido)->int:
    """
    Función que realiza operaciones para encontrar la cantidad de litros que se toman
    en un determinado tiempo.
    :param tiempo_recorrido: Tiempo de recorrido, es dado por el usuario.
    :return: número entero para que sea redondeado.
    """
    resultado = tiempo_recorrido * 0.5
    return int(resultado)
if __name__ == '__main__':
    print(operaciones(1))
    print(operaciones(6.7))
    print(operaciones(11.8))
    print(operaciones(4))