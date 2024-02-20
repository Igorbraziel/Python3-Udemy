import enum

class Direcoes(enum.Enum):
    DIREITA = enum.auto()
    ESQUERDA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()
    
    
def mover(direcao: Direcoes):
    print('movendo para', direcao.name)
    

mover(Direcoes.DIREITA)
mover(Direcoes.ESQUERDA)
mover(Direcoes.ABAIXO)
mover(Direcoes.ACIMA)
    