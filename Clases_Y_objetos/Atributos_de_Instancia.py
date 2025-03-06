"""6 de marzo.
   Hector Jesus Mendez Santiago
   """
class Estudiante:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.temas_aprendidos = []
    def aprender_tema(self, tema:str)->None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre}, aprendio {tema}")
class Profesor:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.temas_dominados = []
    def dominar_tema (self, tema:str):
        self.temas_dominados.append(tema)
        print(f"El profesor {self.nombre} tiene dominio en el tema: {tema}")
    def ensenar_tema (self, no_tema:int)->str:
        tema_a_ensenar = self.temas_dominados[no_tema]
        return tema_a_ensenar