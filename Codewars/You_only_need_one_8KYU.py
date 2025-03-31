"""
-Nobre:-----Hector Jesus
-Descripcion:---Se le dará una matriz a y un valor x. Todo lo que necesita hacer es verificar si la matriz proporcionada contiene el valor.
----------------a puede contener números o cadenas. x puede ser cualquiera.
----------------Devolución true si la matriz contiene el valor, false si no..
"""



def check(seq, elem):
    for prod in seq:
        if elem == prod:
            return True
    return False
    pass