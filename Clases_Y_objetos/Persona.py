"""5 de marzo.
   Hector Jesus Mendez Santiago
   """



class Persona:
    #Constructor
    def __init__(self, nombre:str, edad:int, altura:float, peso:float):
        #Caracteristicas o atributos
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
    #Metodos
    def caminar(self) -> None:
        print(f"{self.nombre} Esta caminando, para bajar sus {self.peso} kgs")

    def comer(self)->None:
        print(f"{self.nombre} anda comiendo platanitos en el comedor, para aumentar su altura de {self.altura}")
    def jugar(self)->None:
        print(f"{self.nombre} esta jugando COD ")
    def dormir(self)->None:
        print(f"{self.nombre} esta durmiendo para tener salud a sus {self.edad} años")


if __name__ == '__main__':
    alberto = Persona("ALbelto", 20, 160.5, 90)
    #Acceder a atributos
    print(alberto.nombre)
    print(alberto.edad)
    print(alberto.altura)
    print(alberto.peso)
    #Acceder a metodos
    alberto.caminar()
    alberto.comer()
    alberto.dormir()
    alberto.jugar()

    #Otro objeto:
    compa_juan = Persona("Juancamaney", 30, 173, 84)
    compa_juan.caminar()
    compa_juan.comer()
    compa_juan.dormir()
    compa_juan.jugar()

    #Acceder a un atributo y modificar
    alberto.peso = 213423
    alberto.caminar()

    print(alberto.nombre)
