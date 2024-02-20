def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return f'{class_name}, {class_dict}'
    cls.__repr__ = my_repr
    return cls

@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
        
@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
        
        
palmeiras = Time('Palmeiras')
terra = Planeta('Terra')
print(palmeiras)
print(terra)