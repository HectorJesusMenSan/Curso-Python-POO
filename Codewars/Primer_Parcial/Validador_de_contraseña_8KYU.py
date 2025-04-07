"""
Descripción
Su trabajo es crear una función de validación de contraseña simple, como se ve en muchos sitios web.

Las reglas para una contraseña válida son las siguientes:

Debe haber al menos 1 letra mayúscula.
Debe haber al menos 1 letra minúscula.
Debe haber al menos 1 número.
La contraseña debe tener al menos 8 caracteres de longitud.
Se le permite utilizar cualquier metodo

Ejemplos:
password("Abcd1234"); ===> true
password("Abcd123"); ===> false
password("abcd1234"); ===> false
password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"); ===> true
password("ABCD1234"); ===> false
password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> true;
password("!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> false;
Información adicional
Solo se te pasarán las cuerdas.
La cadena puede contener cualquier carácter de teclado estándar.
Las cadenas aceptadas pueden tener cualquier longitud, siempre que tengan 8 caracteres o más."""
def password(st:str)->True|False:
    """
    Función que valida una contraseña.
    @param st: cadena o contraseña
    @return: retorna si la contraseña cumple con requisitos.
    """
    mayusculas, minusculas, numeros = 0, 0, 0

    if len(st) > 7:
        for letra in st:
            if letra.isnumeric():
                numeros = 1
            elif letra.islower():
                minusculas = 1
            elif letra.isupper():
                mayusculas = 1
    else:
        return False

    if numeros and mayusculas and minusculas:
        return True
    else:
        return False


