def square_color(file, rank):
    """
    Función que busca la posición de ajedrez y verifica
    si la coordenada introducida esta en una casilla blanca
    o negra.
    @param file:
    @param rank:
    @return:
    """
    diccionario = {'a': [8, 6, 4, 2],
                   'b': [7, 5, 3, 1],
                   'c': [8, 6, 4, 2],
                   'd': [7, 5, 3, 1],
                   'e': [8, 6, 4, 2],
                   'f': [7, 5, 3, 1],
                   'g': [8, 6, 4, 2],
                   'h': [7, 5, 3, 1]}
    for key, value in diccionario.items():
        if file == key:
            if rank in value:
                return "white"

    return 'black'