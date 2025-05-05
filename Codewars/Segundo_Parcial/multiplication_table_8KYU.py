

def multi_table(number):
    """
    Función que genera una tabla de multiplicar,dependeiendo del número que se ingrese
    @param number:
    @return:
    """
    lines = []
    for i in range(1, 11):
        lines.append(f"{i} * {number} = {i * number}")
    return "\n".join(lines)