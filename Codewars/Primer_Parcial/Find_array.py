
"""
Se le dan dos matrices arr1 y arr2, donde arr2 siempre contiene enteros.

Escribe una función tal que:

Para arr1 = ['a', 'a', 'a', 'a', 'a'], arr2 = [2, 4] la función devuelve ['a', 'a']

Para arr1 = [0, 1, 5, 2, 1, 8, 9, 1, 5], arr2 = [1, 4, 7] la función devuelve [1, 1, 1]

Para arr1 = [0, 3, 4], arr2 = [2, 6] la función devuelve [4]

Para arr1=["a","b","c","d"] , arr2=[2,2,2], la función devuelve ["c","c","c"]

Para arr1=["a","b","c","d"], arr2=[3,0,2] la función devuelve ["d","a","c"]

Tenga en cuenta que cuando un elemento dentro arr2 es mayor que el índice del último elemento de arr1 ningún elemento de arr1 debe añadirse a la matriz resultante. Si alguno arr1 o arr2 está vacío, debe devolver un arr vacío (lista vacía en python, vector vacío en c++). Nota para c++ use std::vector arr1, arr2.


"""

def funcion (lista1, lista2):
    """
    Función que recibe dos listas, la segunda tiene los índices para imprimir los datos de la primera lista.
    @param lista1: Lista original.
    @param lista2: Lista con los índices.
    @return: lista datos indicados.
    """
    lisra3=[]

    for numero in lista2:
        if numero < len(lista1):
            lisra3.append(lista1[numero])
    return  lisra3
if __name__ == '__main__':
    lista1=["1", "arr", "$"]
    lista2 = [1,2]
    print(funcion(lista1, lista2))

