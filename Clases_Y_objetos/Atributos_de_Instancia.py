"""6 de marzo.
   Hector Jesus Mendez Santiago
      Programacion orientada a objetos: Programa que crea objetos

   """
class Estudiante:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.temas_aprendidos = []
    def aprender_tema(self, tema:str)->None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre}, aprendio {tema}")

    #Metodo magico: Le decimos que queremos que imprima
    def __str__(self)->None:
        return f"Estudiante(nombre:{self.nombre}, temas_aprendidos:{self.temas_aprendidos})"

class Profesor:
    def __init__(self, nombre:str, temas_dominados:list[str]):
        self.nombre = nombre
        self.temas_dominados = temas_dominados
    def dominar_tema (self, tema:str):
        self.temas_dominados.append(tema)
        print(f"El profesor {self.nombre} tiene dominio en el tema: {tema}")
    def ensenar_tema (self, no_tema:int)->str:

        if no_tema>len(self.temas_dominados):
            return "Fuera de rango"
        else:
            tema_a_ensenar = self.temas_dominados[no_tema]
            return tema_a_ensenar

    #Metodo magico
    def __str__(self)->None:
        return f"Profesor(Nombre: {self.nombre}, temas_dominados: {self.temas_dominados})"

if __name__ == '__main__':
    estudiante1 = Estudiante("Albelto")
    estudiante2 = Estudiante("Addi")
    estudiante1.aprender_tema("Evolucion sitios web")
    estudiante2.aprender_tema("IoT")

    print(estudiante1)
    print(estudiante2)
    #Metodo magico

    profesor1 = Profesor("ALLLbelto mayor", ["poo", "teoria del basketball", "futbol profesional"])
    print(profesor1)



