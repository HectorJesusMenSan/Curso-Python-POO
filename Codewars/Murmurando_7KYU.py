"""
Hector Jeús Méndez Satiago
Esta vez no hay historia, no hay teoría. Los ejemplos a continuación le muestran cómo escribir la función accum:

Ejemplos:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
El parámetro de accum es una cadena que incluye solo letras de a..z y A..Z.
"""
from os import remove

def accum(st):
    lista = []
    for i in range(len(st)):
        if i == 0:
            lista.append(st[i].upper())
            lista.append("-")
        else:
            palabra = st[i] * (1+i)
            palabra = list(palabra)
            for j in range(len(palabra)):
                if j == 0:
                    palabra[j] = palabra[j].upper()
                else:
                    palabra[j] = palabra[j].lower()
            palabra = "".join(palabra)

            lista.append(palabra)

            lista.append("-")
    lista.pop( len(lista) - 1 )

    lista = "".join(lista)

    return lista

if __name__ == '__main__':
    print(accum("aperrosyidsfgsdfg"))