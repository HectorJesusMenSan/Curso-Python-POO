def encode(text):
    """
    Reemplaza vocales minúsculas por números según:
    a->1, e->2, i->3, o->4, u->5
    """
    mapa = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    resultado = ''
    for letra in text:
        resultado += mapa.get(letra, letra)  # reemplaza si está en el mapa, si no la deja igual
    return resultado

def decode(text):
    """
    Reemplaza números por sus vocales correspondientes:
    1->a, 2->e, 3->i, 4->o, 5->u
    """
    mapa = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    resultado = ''
    for letra in text:
        resultado += mapa.get(letra, letra)
    return resultado