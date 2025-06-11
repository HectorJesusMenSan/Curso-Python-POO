def string_to_int_list(s):
    """
    Toma una cadena con números separados por comas y devuelve una lista de enteros,
    ignorando comas vacías o consecutivas.
    """
    resultado = []            # Lista donde se guardarán los números
    numero = ''               # Cadena temporal para construir cada número

    for caracter in s:
        if caracter != ',':
            numero += caracter    # Agregamos dígito o signo
        else:
            if numero != '':      # Si hay un número listo, convertimos
                resultado.append(int(numero))
                numero = ''       # Reiniciamos

    # puede que haya un número pendiente sin una coma al final
    if numero != '':
        resultado.append(int(numero))

    return resultado