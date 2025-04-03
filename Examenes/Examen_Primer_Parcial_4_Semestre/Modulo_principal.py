from colorama import Fore, Back, Style
from reportlab.lib.colors import forestgreen

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
        print("No hay jugadores")
def ver_equipos(equipos):
    if len(equipos)>0:
        print(Fore.BLUE + "Todos los Equipos son: ")
        contador = 0
        for equipo in equipos:
            print(Fore.YELLOW + f"{contador}).{equipo.nombre}")
    else:
        print("No hay equipos.")

def menu_principal():
    jugadores  = []
    equipos = []
    champions_league = Torneo("champions League")

    opcion = None
    while opcion != 0:
        opcion = menu_interactivo()
        if opcion == 1:
            nombre_jugador = input(Fore.CYAN + "Ingrese el nombre del nuevo jugador: ")
            numero_jugador = int(input(Fore.CYAN + "Ingresa el número del nuevo jugador: "))
            jugador = Jugador(nombre_jugador, numero_jugador)
            jugadores.append(jugador)
        elif opcion == 2:
            nombre_equipo = input(Fore.CYAN + "Ingresa nombre de equipo: ")
            equipo = Equipo(nombre_equipo)
            equipos.append(equipo)
        elif opcion == 3:
            ver_jugadores(jugadores)
        elif opcion == 4:
            ver_equipos(equipos)
        elif opcion == 5:   #Agregar jugador a equipo
            ver_equipos(equipos)
            if len(equipos)>0:
                escoger_equipo = int(input("Escoge el equipo: "))
                contador = int(input("Cuantos jugadores deceas meter? : "))

                if contador>0:
                    for i in range(0, contador):
                        ver_jugadores(jugadores)
                        jugador_seleccionado = int(input("Ingresa jugador a agregar: "))
                        equipos[escoger_equipo].agregar_jugadores(jugadores[jugador_seleccionado])
                else:
                    print("No hay cantidad de jugadores a agregar.")
            else:
                print("Error.")

        elif opcion == 6:   #Eliminar jugador de equipo
            ver_equipos(equipos)
            if len(equipos)>0:
                escoger_equipo = int(input("Escoge el equipo: "))
                contador = int(input("Cuantos jugadores deseas eliminar? : "))

                if contador>0:
                    for i in range(0, contador):
                        ver_jugadores(equipos[escoger_equipo].jugadores)
                        jugador_seleccionado = int(input("Ingresa jugador a eliminar: "))
                        equipos[escoger_equipo].remover_jugadores(jugadores[jugador_seleccionado])
                        print(f"{jugadores[jugador_seleccionado]}, se elimino. ")
                else:
                    print("No hay cantidad de jugadores a agregar.")
            else:
                print("Error.")

        elif opcion == 7:#Agregar equipos a torneo

            if len(equipos)>0:

                contador = int(input("Cuantos equipos inscribiras al torneo?: "))
                for i in range(0, contador):
                    ver_equipos(equipos)
                    escoger_equipo = int(input("Que equipo inscribiras: "))
                    champions_league.agregar_equipos(equipos[escoger_equipo])
                    print(f"Se agrego el equipo {equipos[escoger_equipo]} al torneo {champions_league.nombre}")
            else:
                print("Error")
        elif opcion == 8:
            if len(equipos) > 0:

                contador = int(input("Cuantos equipos eliminaras del torneo?: "))
                for i in range(0, contador):
                    ver_equipos(equipos)
                    escoger_equipo = int(input("Que equipo eliminaras: "))
                    champions_league.remover_equipos(equipos[escoger_equipo])
                    print(f"Se agrego el equipo {equipos[escoger_equipo]} al torneo {champions_league.nombre}")
            else:
                print("Error")
        elif opcion == 9:
            if len(jugadores)>0:
                ver_jugadores(jugadores)
                jugador_a_anotar = int(input("A que jugador anotaras goles?: "))
                anotar_gol = int(input("Cuantos goles se anotaran?: "))
                jugadores[jugador_a_anotar].anotar_goles(anotar_gol)
            else:
                print("Eror....")
        elif opcion == 10:

            if len(equipos)>0:
                ver_equipos(equipos)
                escoger_equipo = int(input("Escoge equipo: "))
                equipos[escoger_equipo].total_de_goles()
            else:
                print("Error")

        elif opcion == 11:
            champions_league.generar_rol()
            pass
        elif opcion == 0:
            pass
        else:
            print(Fore.RED + "Error, fuera de rango...")


if __name__ == '__main__':
    menu_principal()