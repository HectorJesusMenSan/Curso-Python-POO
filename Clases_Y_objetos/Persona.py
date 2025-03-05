



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
        print("Estoy caminando")
    def comer(self)->None:
        print("Estoy comiendo")
    def jugar(self)->None:
        print("Estoy jugando")
    def dormir(self)->None:
        print("Estoy durmiendo")


if __name__ == '__main__':
    alberto = Persona("ALbelto", 20, 160.5, 90)
    #Acceder a atributos
    print(alberto.nombre)
    print(alberto.edad)
    print(alberto.altura)
    print(alberto.peso)
    #Acceder a metodos
    alberto.caminar()
