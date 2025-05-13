def powers(n):
    """
    Funión que calcula las sumas de potencias hasta llegar a numero
    ingresado

    @param n:
    @return:
    """
    resultado = []
    i = 0
    while n > 0:
        if n % 2 == 1:
            resultado.append(2**i)
        n = n // 2
        i += 1
    return resultado