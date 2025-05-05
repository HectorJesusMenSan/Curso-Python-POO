def sum_str(a, b):
    """
    Función que retorna la suma de dos entradas de cadenas
    @param a:
    @param b:
    @return:
    """
    if a == "":
        a = "0"
    if b == "":
        b = "0"

    suma = int(a) + int(b)
    return str(suma)
