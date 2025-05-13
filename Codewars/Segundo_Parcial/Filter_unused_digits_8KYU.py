



def unused_digits(*numbers):
    """
    -Funcion para filtrar numeros que no se usan
    Parameters
    ----------
    numbers
    """
    numeros = list(numbers)
    numeros_validos = [1,2,3,4,5,6,7,8,9,0]
    numeros_invalidos = []
    for numero in numeros:
        if numero in numeros_validos:
            numeros_invalidos(numero)
    letras = "".join(numeros_invalidos)
    print(letras)
    #your code here

if __name__ == '__main__':
    unused_digits(1,2,3,4,5,6,7,8)