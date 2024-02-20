class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.x}, {self.y})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other) -> bool:
        resultado1 = self.x + self.y
        resultado2 = other.x + other.y
        if resultado1 > resultado2:
            return True
        else:
            return False
        
    def __lt__(self, other) -> bool:
        resultado1 = self.x + self.y
        resultado2 = other.x + other.y
        if resultado1 < resultado2:
            return True
        else:
            return False
        
    
p1 = Ponto(2, 7)
p2 = Ponto(78, 29)
p3 = p1 + p2
print(p3)
print('P1 é menor que P2?', p1 < p2)
print('P1 é maior do que P2?', p1 > p2)