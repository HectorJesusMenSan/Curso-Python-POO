"""11 de marzo.
   Hector Jesus Mendez Santiago
      Programación orientada a objetos: Programa que crea objetos
      Se relaciona con las clases
      __no_id___:int = Indica que es un tributo de clase
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
    def __str__(self)->None:
        return f"Empleado: {self.nombre}, id: {self.id}, sueldo:{self.sueldo}"


if __name__ == '__main__':
    empleado1 = Empleado("Albelto", 123.3)
    empleado2 = Empleado("addi", 500.654)

    print(empleado1.no_id)

    print(empleado1)
    print(empleado2)
    print(f"Atributo de clase: {Empleado.no_id = }")