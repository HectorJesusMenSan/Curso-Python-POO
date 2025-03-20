
"""19 de marzo.
    Hector Jesus Mendez Santiago
    Programacion orientada a objetos: Programa que crea objetos
    Se relaciona con las clases.
    relación uno a muchos, relacion de agregacion

"""


class Empleado:
    no_id = 1
    def __init__(self, nombre:str, sueldo:float ):
        self.nombre= nombre
        self.sueldo= sueldo
        self.id = Empleado.no_id
        Empleado.no_id += 1
    def aumentar_sueldo (self, porcentaje:float)->None:
        pass

    def __str__(self)->str:
        return f"Empleado: {self.nombre}, id: {self.id}, sueldo:{self.sueldo}"

class Empresa:
    def __init__(self, nombre:str, *empleados:Empleado)->None:
        self.nombre =nombre
        self.empleados = list(empleados)
    def agregar_empleados (self, *nuevos_empleados:Empleado):
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"

    def mostrar_empleados(self) -> None:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        print(f"*** Lista de empleados de {self.nombre} ***")

        for empleado in self.empleados:
            print(empleado)


if __name__ == '__main__':
    alberto = Empleado("alberto", 125.50)
    print(alberto)
    addi = Empleado("Adrian", 345.50)
    print(addi)

    unsij = Empresa("Unsij", alberto, addi)
    unsij.mostrar_empleados()
    print(unsij)
    alberto.nombre = "AAALLLLBEEELTTOOOO"
    print(alberto)
    print(alberto.nombre)
    #Cambiar nombres (Capsulas)
    #Set para acceder
    #Get para ver

