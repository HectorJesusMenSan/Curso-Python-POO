"""
Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"
"""




def replace_exclamation(st: str)->str:
    """
    Elimina vocales de una cadena, devuelve una cadena y recibe una cadena
    """


    lista_vocales = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    st = list(st)
    for i in range(len(st)):
        if st[i] in lista_vocales:
            st[i] = "!"
    st = "".join(st)
    return st


if __name__ == '__main__':
    st = input("Ingresa cadena: ")
    replace_exclamation(st)
