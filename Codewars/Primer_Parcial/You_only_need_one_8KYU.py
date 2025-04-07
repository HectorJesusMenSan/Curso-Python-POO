"""
-Nombre:-----Hector Jesus
-Descripción:---Se le dará una matriz a y un valor x. Todo lo que necesita hacer es verificar si la matriz proporcionada contiene el valor.
----------------a puede contener números o cadenas. x puede ser cualquiera.
----------------Devolución true si la matriz contiene el valor, false si no.
"""



def check(seq:list, elem:str)->True|False:
    """
    Función que determina si un elemento está dentro de una cadena o lista
    @param seq: lísta o cadena
    @param elem: elemento a buscar
    @return:True|False
    """
    for prod in seq:
        if elem == prod:
            return True
    return False
    pass