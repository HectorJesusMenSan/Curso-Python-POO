def invert_hash(dictionary):
    """
    Recibe un diccionario y devuelve uno nuevo con claves y valores invertidos.
    """
    inverted = {}
    for key in dictionary:
        value = dictionary[key]
        inverted[value] = key
    return inverted
