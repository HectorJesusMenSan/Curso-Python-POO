def obfuscate(email):
    """Función que reemplaza el punto y el arroba en
    otras palabras"""
    list = []
    for car in email:
        if car == "@":

            # print(" [at]", end=" ")
            list.append(" [at] ")
        elif car == ".":
            # print(" [dot]", end=" ")
            list.append(" [dot] ")
        else:
            # print(f"{car}", end="")
            list.append(f"{car}")
    list = "".join(list)

    return list_