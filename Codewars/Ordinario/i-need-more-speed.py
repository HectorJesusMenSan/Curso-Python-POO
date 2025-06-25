
def reverse(arr):
    """
    Revierte el arreglo dado en su lugar.

    Esta función modifica el arreglo original intercambiando los elementos
    desde el principio hasta el final sin crear un nuevo arreglo.
    """
    if len(arr) > 1:  # Si la lista está vacía o tiene un solo elemento, no hay nada que hacer


        left = 0
        right = len(arr) - 1

        while left < right:
            # Intercambiar los elementos
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            # Mover los índices
            left += 1
            right -= 1