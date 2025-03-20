"""20 de marzo.
    Hector Jesus Mendez Santiago
    Programacion orientada a objetos: + Publico
    _ o # atributo asegurado o protegido
    diagrama de ...
"""

class CuentaBancaria:
    def __init__(self, titular:str, saldo_inicial:float=0):
        self.titular = titular
        #Bloquear variable
        self._saldo = saldo_inicial
    def depositar(self, cantidad:float):
        self._saldo += cantidad
    def retirar(self, cantidad:float):
        if self._saldo>=cantidad:
            self._saldo -= cantidad
    def __int__(self):
        return f"El titular es {self.titular}, su saldo es{self._saldo}"
    #Propiedad: get
    @property
    def saldo (self)->float:
        return self._saldo

    #Set:
    @saldo.setter
    def saldo (self, nuevo_saldo:float):
        self._saldo = nuevo_saldo

if __name__ == '__main__':
    cueta_guadalupe = CuentaBancaria("Guadalupe")
    print(cueta_guadalupe.saldo)

