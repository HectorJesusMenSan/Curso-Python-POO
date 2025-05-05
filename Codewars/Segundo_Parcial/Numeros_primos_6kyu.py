"""Ejercicio: Kata nivel 6Kyu"""
def is_prime (number: int)->bool:
    """
    Función que verifica si un número es primo
    @param number:
    @return:
    """

    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    num = int(input("Ingresa numero:"))
    if is_prime(num):
        print("Si")
    else:
        print("no")