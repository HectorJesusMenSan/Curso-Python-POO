#SayHEllo
def greet(name):
    """
    Función que concatena un hola a un nombre.
    @param name:
    @return:
    """
    if not name:
        return None
    else:
        return f"hello {name}!"