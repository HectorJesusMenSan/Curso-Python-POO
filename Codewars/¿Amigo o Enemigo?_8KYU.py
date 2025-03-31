"""
Haga un programa que filtre una lista de cadenas y devuelva una lista con solo el nombre de sus amigos.

Si un nombre tiene exactamente 4 letras, ¡puedes estar seguro de que tiene que ser un amigo tuyo! De lo contrario, puedes estar seguro de que no...

Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

Input = ["Peter", "Stephen", "Joe"]
Output = []
Las cadenas de entrada solo contendrán letras.
Nota: mantenga el orden original de los nombres en la salida.
"""


def friend(x):
    #Code
    lista_de_amigos=[]
    for nombre in x:
        if len(nombre)==4:
            lista_de_amigos.append(nombre)
    return lista_de_amigos
if __name__ == '__main__':
    lst = ["nombre","hector"]
    print(friend(lst))