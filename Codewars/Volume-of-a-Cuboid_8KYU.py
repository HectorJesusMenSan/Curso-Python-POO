"""Volume of a Cuboid
Bob necesita una forma rápida de calcular el volumen de un cuboide rectangular con tres valores: el length, width y height del cuboide.

Escribe una función para ayudar a Bob con este cálculo.


"""


def get_volume_of_cuboid(length:float, width:float, height:float)->int:
    """
    Función que imprime calcula el volumen de un cubo
    :param length: largo
    :param width: ancho
    :param height: altura
    :return: retorna el resultado
    """
    return length * width * height

if __name__ == '__main__':
    length = int(input("Ingresa length "))
    width= int(input("Ingresa width "))
    height= int(input("Ingresa height "))
    print(get_volume_of_cuboid(length, width, height))

