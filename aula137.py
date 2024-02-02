class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        

    def mostrar_carro(self):
        print(self.nome)
        print(self.motor.nome, f"{self.motor.potencia}V")
        print(self.fabricante.nome)
                

class Motor:
    def __init__(self, nome, pot):
        self.nome = nome
        self.potencia = pot
        

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
        
car = Carro("Fusca")
motor = Motor("turbina", 220)
fabricante = Fabricante("Volkswagen")

car.motor = motor
car.fabricante = fabricante
car.mostrar_carro()