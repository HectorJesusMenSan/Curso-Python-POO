"""
Héctor Jesús Méndez Santiago

Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""


def maps(a:list)->list:
    """
    Función que duplica elementos de una lista de números enteros
    @param a: lista de números
    @return:  lista de números duplicádos
    """
    for numero in range(len(a)):
        a[numero]*=2
    return a
if __name__ == '__main__':
    lista=[1,2,3,4]
    print(maps(lista))
