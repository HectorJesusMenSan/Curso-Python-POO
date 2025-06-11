def largest_sum(s):
    """
    Recibe una cadena de dígitos terminada en 0.
    Divide en subcadenas separadas por ceros y devuelve la mayor suma de sus dígitos.
    """
    max_suma = 0       # Lleva el registro de la suma máxima
    actual = 0         # Suma temporal para la subcadena actual

    for caracter in s:
        if caracter == '0':
            if actual > max_suma:
                max_suma = actual
            actual = 0  # Reiniciar suma para la siguiente subcadena
        else:
            actual += int(caracter)  # Sumar el dígito actual

    return max_suma