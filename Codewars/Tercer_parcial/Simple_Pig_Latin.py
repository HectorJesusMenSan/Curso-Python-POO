def pig_it(text):
    """
    Mueve la primera letra de cada palabra al final y agrega 'ay'.
    No modifica signos de puntuación.
    """
    palabras = text.split()
    resultado = []

    for palabra in palabras:
        if palabra.isalpha():
            nueva = palabra[1:] + palabra[0] + 'ay'
            resultado.append(nueva)
        else:
            resultado.append(palabra)  # dejar signos intactos

    return ' '.join(resultado)