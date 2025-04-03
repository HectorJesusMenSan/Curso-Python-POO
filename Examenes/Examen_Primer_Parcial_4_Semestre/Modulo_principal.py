from colorama import Fore, Back, Style


from Examenes.Examen_Primer_Parcial_4_Semestre.Modulo_Equios import Equipo
from Examenes.Examen_Primer_Parcial_4_Semestre.Modulo_Jugador import Jugador
from Examenes.Examen_Primer_Parcial_4_Semestre.Modulo_Torneo import Torneo


def menu_interactivo():

    print(Fore.GREEN + "\t______________________________________________")
    print(Fore.GREEN + "\t______________________________________________")
    print(Fore.GREEN + "\t---|Bienvenido al torneo: Champions League|---")
    print(Fore.GREEN + "\t______________________________________________")
    print(Fore.GREEN + "\t______________________________________________")
    print(Fore.BLUE + "\t::::::::::[1]. Crea nuevo Jugador:::::::::::::")
    print(Fore.BLUE + "\t::::::::::[2]. Crea nuevo Equipo::::::::::::::")
    print(Fore.BLUE + "\t::::::::::[3]. Ver lista de jugadores:::::::::")
    print(Fore.BLUE + "\t::::::::::[4]. Ver lista de equipos:::::::::::")
    print(Fore.BLUE + "\t::::::::::[5]. Agregar jugadores a un equipo::")
    print(Fore.BLUE + "\t::::::::::[6]. Eliminar jugador de equipo::")
    print(Fore.BLUE + "\t::::::::::[7]. Agregar equipos al torneo::::::")
    print(Fore.BLUE + "\t::::::::::[8]. Eliminar equipos del torneo::::")
    print(Fore.BLUE + "\t::::::::::[9]. Anotar goles a un jugador::::::")
    print(Fore.BLUE + "\t::::::::::[10]. Conocer goles totales de equipo ")
    print(Fore.BLUE + "\t::::::::::[11]. Generar rol de juegos:::::::::: ")
    print(Fore.BLUE + "\t::::::::::[0]. Salir:::::::::::::::::::::::::: ")
    print(Fore.GREEN + "\t______________________________________________")

    opcion = input(Fore.LIGHTYELLOW_EX+"\tIngresa opción deseada: ")
    while not opcion.isnumeric():
        opcion = input(Fore.RED + "\tError... Ingrese de nuevo: ")
    opcion = int(opcion)
    print(Fore.GREEN + "\t______________________________________________")
    return opcion

def ver_jugadores (jugadores):

    contador = 0
    if len(jugadores)>0:
        print(Fore.BLUE + "Todos los jugadores son: ")
        for jugador in jugadores:

            print(Fore.YELLOW + f"{contador}).{jugador.nombre}")
            contador += 1
    else:
        print(Fore.RED + "\n\tNo hay jugadores")
def ver_equipos(equipos):
    if len(equipos)>0:
        print(Fore.BLUE + "Todos los Equipos son: ")
        contador = 0
        for equipo in equipos:
            print(Fore.YELLOW + f"{contador}).{equipo.nombre}")
            contador += 1
    else:
        print(Fore.RED + "\n\tNo hay equipos.")

def validar_numeros (numero:str)->int:
    while not  numero.isnumeric():
        numero = input(Fore.RED + "Error, intenta otra vez: ")
    return int(numero)
def validar_letras (palabra:str)->str:
    while not  palabra.isalpha():
        palabra = input(Fore.RED + "Error, intenta otra vez: ")
    return str(palabra)
def menu_principal():
    jugadores  = []
    equipos = []
    champions_league = Torneo("champions League")

    opcion = None
    while opcion != 0:
        opcion = menu_interactivo()
        if opcion == 1:
            nombre_jugador = input(Fore.CYAN + "Ingrese el nombre del nuevo jugador: ")
            nombre_jugador = validar_letras(nombre_jugador)
            numero_jugador = input(Fore.CYAN + "Ingresa el número del nuevo jugador: ")
            numero_jugador = validar_numeros(numero_jugador)
            jugador = Jugador(nombre_jugador, numero_jugador)
            print(Fore.GREEN + f"\n\tEl jugador: {jugador.nombre}, fue creado exitosamente.")
            jugadores.append(jugador)
        elif opcion == 2:
            nombre_equipo = input(Fore.CYAN + "Ingresa nombre de equipo: ")
            nombre_equipo = validar_letras(nombre_equipo)
            equipo = Equipo(nombre_equipo)
            print(Fore.GREEN + f"\n\tEl equipo: {equipo.nombre} fue creado.")
            equipos.append(equipo)
        elif opcion == 3:
            ver_jugadores(jugadores)
        elif opcion == 4:
            ver_equipos(equipos)
        elif opcion == 5:   #Agregar jugador a equipo

            if len(equipos)>0:
                ver_equipos(equipos)
                escoger_equipo = input("Escoge el equipo: ")
                escoger_equipo = validar_numeros(escoger_equipo)
                while escoger_equipo > len(equipos)-1:
                    escoger_equipo = input(Fore.RED + "Error, fuera de rango: ")
                    escoger_equipo = validar_numeros(escoger_equipo)

                ver_jugadores(jugadores)
                contador = input("Cuantos jugadores deseas meter? : ")
                contador = validar_numeros(contador)
                while contador > len(jugadores):
                    contador = input(Fore.RED + "Error, fuera de rango: ")
                    contador = validar_numeros(contador)

                if contador>0:

                    for i in range(0, contador):

                        jugador_seleccionado = input("Ingresa jugador a agregar: ")
                        jugador_seleccionado = validar_numeros(jugador_seleccionado)
                        while jugador_seleccionado > len(jugadores)-1:
                            jugador_seleccionado = input(Fore.RED + "Error, fuera de rango: ")
                            jugador_seleccionado = validar_numeros(jugador_seleccionado)

                        equipos[escoger_equipo].agregar_jugadores(jugadores[jugador_seleccionado])
                        print(Fore.GREEN + f"El {jugadores[jugador_seleccionado].nombre} se agredo al {equipos[escoger_equipo].nombre}")
                else:
                    print(Fore.RED + "\n\tNo hay cantidad de jugadores a agregar.")
            else:
                print(Fore.RED + "\n\tError, no hay elementos...")

        elif opcion == 6:   #Eliminar jugador de equipo
            if len(equipos)>0:
                ver_equipos(equipos)
                escoger_equipo = input("Escoge el equipo: ")
                escoger_equipo = validar_numeros(escoger_equipo)
                while escoger_equipo>len(equipos)-1:
                    escoger_equipo = input(Fore.RED + "Error, fuera de rango: ")
                    escoger_equipo = validar_numeros(escoger_equipo)


                if len(equipos[escoger_equipo].jugadores) > 0:
                    contador = input("Cuantos jugadores deseas eliminar? : ")
                    contador = validar_numeros(contador)
                    while contador > len(equipos[escoger_equipo].jugadores):
                        contador = input(Fore.RED + "Error, fuera de rango: ")
                        contador = validar_numeros(contador)

                    if contador>0:
                        for i in range(0, contador):

                            ver_jugadores(equipos[escoger_equipo].jugadores)
                            jugador_seleccionado = input("Ingresa jugador a eliminar: ")
                            jugador_seleccionado = validar_numeros(jugador_seleccionado)
                            while jugador_seleccionado > len(equipos[escoger_equipo].jugadores) - 1:
                                jugador_seleccionado = input(Fore.RED + "Error, fuera de rango: ")
                                jugador_seleccionado = validar_numeros(jugador_seleccionado)

                            equipos[escoger_equipo].remover_jugadores(equipos[escoger_equipo].jugadores[jugador_seleccionado])
                            print(f"{jugadores[jugador_seleccionado].nombre}, se elimino. ")
                    else:
                        print(Fore.RED + "\n\tNo hay cantidad de jugadores a eliminar.")
                else:
                    print(Fore.RED + "\n\tError: No hay jugadores en equipo")
            else:
                print(Fore.RED + "\n\tError, no hay equipos...")

        elif opcion == 7:#Agregar equipos a torneo

            if len(equipos)>0:
                ver_equipos(equipos)
                contador = input("Cuantos equipos inscribiras al torneo?: ")
                contador = validar_numeros(contador)
                while contador > len(equipos):
                    contador = input(Fore.RED + "Error, fuera de rango: ")
                    contador = validar_numeros(contador)

                for i in range(0, contador):
                    ver_equipos(equipos)
                    escoger_equipo = input("Que equipo inscribiras: ")
                    escoger_equipo = validar_numeros(escoger_equipo)
                    while escoger_equipo > len(equipos)-1:
                        escoger_equipo = input("Que equipo inscribiras: ")
                        escoger_equipo = validar_numeros(escoger_equipo)

                    champions_league.agregar_equipos(equipos[escoger_equipo])
                    print(f"Se agrego el equipo {equipos[escoger_equipo].nombre} al torneo {champions_league.nombre}")
            else:
                print(Fore.RED + "\n\tError, no se agregaran equipos.")

        elif opcion == 8:
            if len(equipos) > 0:
                ver_equipos(champions_league.equipos)
                contador = input("Cuantos equipos eliminaras del torneo?: ")
                contador = validar_numeros(contador)
                while contador>len(champions_league.equipos):
                    contador = input(Fore.RED + "Error. fuera de rango: ")
                    contador = validar_numeros(contador)

                for i in range(0, contador):
                    ver_equipos(champions_league.equipos)
                    escoger_equipo = input("Que equipo eliminaras: ")
                    escoger_equipo = validar_numeros(escoger_equipo)
                    while escoger_equipo> len(champions_league.equipos)-1:
                        escoger_equipo = input("Error fuera de rango: ")
                        escoger_equipo = validar_numeros(escoger_equipo)
                    champions_league.remover_equipos(equipos[escoger_equipo])
                    print(f"Se elimino el equipo {equipos[escoger_equipo]} al torneo {champions_league.nombre}")
            else:
                print(Fore.RED + "\n\tError, no hay equipos que agregar.")
        elif opcion == 9:
            if len(jugadores)>0:
                ver_jugadores(jugadores)
                jugador_a_anotar = input("A que jugador anotaras goles?: ")
                jugador_a_anotar = validar_numeros(jugador_a_anotar)
                anotar_gol = input("Cuantos goles se anotaran?: ")
                anotar_gol = validar_numeros(anotar_gol)
                jugadores[jugador_a_anotar].anotar_goles(anotar_gol)
            else:
                print(Fore.RED + "\n\tError, no existen jugadores...")
        elif opcion == 10:

            if len(equipos)>0:
                ver_equipos(champions_league.equipos)
                escoger_equipo = input("Escoge equipo: ")
                escoger_equipo = validar_numeros(escoger_equipo)
                while escoger_equipo>len(champions_league.equipos)-1:
                    escoger_equipo = input("Error. Escoge equipo: ")
                    escoger_equipo = validar_numeros(escoger_equipo)

                champions_league.equipos[escoger_equipo].total_de_goles()
            else:
                print(Fore.RED + "\n\tError, fuera de rango...")

        elif opcion == 11:
            champions_league.generar_rol()

        elif opcion == 0:
            print(Fore.LIGHTMAGENTA_EX + "Salida exitosa")
        else:
            print(Fore.RED + "\n\tError, fuera de rango...")


if __name__ == '__main__':
    menu_principal()