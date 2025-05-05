def even_or_odd(number: int)->str:
    """
    Función que verifica que número es par
    @param number: Numero recibido
    @return: Mensaje en caso de que sea par o inpar
    """
    bandera = "Odd"
    if number %2 == 0:
        bandera = "Even"
    return bandera
