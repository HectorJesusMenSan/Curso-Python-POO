def solution(number):
    """
    Función que recibe un número que delimita el final de los números
    que se deben calcular si son múltiplos de 3 o 5
    @param number: Número que delimita el final o el rango
    @return: Números múltiplos de 3 o 5, en caso de que el rango sea
    negativo retorna 0.

    """
    acum = 0
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            acum += i
        elif i < 0:
            return 0
    return acum
    pass
