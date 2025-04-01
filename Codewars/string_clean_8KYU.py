"""
Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your database. At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.

Examples (input -> output)
'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 great!' -> 'This looks great!'
Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.
"""


def string_clean(s:str)->str:
    """
    Función que limpia los números de una cadena.
    @param s: Se recibe una cadena.
    @return: Retornamos una cadena.
    """
    # Your code here

    lista = []
    for palabra in s:
        if not palabra.isnumeric():
            lista.append(palabra)
    lista = "".join(lista)
    return lista

if __name__ == '__main__':
    print(string_clean("acasdcasdnm1234"))