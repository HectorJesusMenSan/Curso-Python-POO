




def people_with_age_drink(age:int)->str:
    """
    Función que calcula que bebida se debe tomar a una edad respectiva.
    @param age: Edad ingresada
    @return: Mensaje de la bebida que debe tomar
    """
    if age < 14:
        return "drink toddy"
    elif age>=14 and age<18:
        return "drink coke"
    elif age>=18 and age<21:
        return "drink beer"
    else:
        return "drink whisky"

if __name__ == '__main__':
    print(people_with_age_drink(45))