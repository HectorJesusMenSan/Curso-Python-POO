def comes_after(st, l):
    """
    Devuelve una cadena formada por las letras que siguen a cada aparición de `letter`,
    ignorando signos, números o guiones bajos.
    """
    resultado = ""
    letra = l.lower()

    for i in range(len(st) - 1):  # hasta el penúltimo carácter
        if st[i].lower() == letra:
            siguiente = st[i + 1]
            if siguiente.isalpha():  # solo se aceptan letras
                resultado += siguiente

    return resultado