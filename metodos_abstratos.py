from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, nome):
        self._name = None
        self.name = nome
        
    @property
    @abstractmethod
    def name(self):
        ...
        
        
class Foo(AbstractFoo):
    def __init__(self, nome):
        super().__init__(nome)
        print('Sou inutil')
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        
foo = Foo('igor')
print(foo.name)