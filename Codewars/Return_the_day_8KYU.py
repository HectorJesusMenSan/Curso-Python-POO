"""
Complete la función que devuelve el día de la semana de acuerdo con el número de entrada:

1 devoluciones "Sunday"
2 devoluciones "Monday"
3 devoluciones "Tuesday"
4 devoluciones "Wednesday"
5 devoluciones "Thursday"
6 devoluciones "Friday"
7 devoluciones "Saturday"
De lo contrario, devuelve "Wrong, please enter a number between 1 and 7"
"""

def whatday(num:int)->str:
    """
    Función que devuelve el día dependiendo del número ingresado. Rango 1-7.
    @param num: Número del día
    @return:  de la semana
    """
  # Put your code here
    while not num in range(1, 7):
        num = input("Wrong, please enter a number between 1 and 7")
        num = int(num)
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    else:
        return "Saturday"

if __name__ == '__main__':
    print(whatday(9))