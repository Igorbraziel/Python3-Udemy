from abc import ABC, abstractmethod
from typing import List

from random import choice

class Abstract(ABC):
    def template_method(self):
        self.operation2(self.operation1())
        
    @abstractmethod
    def operation1(self) -> List: ...
    
    @abstractmethod
    def operation2(self, list: List) -> None: ...    
    
    
class ConcreteClass1(Abstract):
    def operation1(self) -> List:
        return [
            choice([value for value in range(300)]) for _ in range(10)
        ]
    
    def operation2(self, list: List) -> None:
        list.sort(reverse=True)
        print(list)
        

class ConcreteClass2(Abstract):
    def operation1(self) -> List:
        return [
            choice([value for value in range(1000)]) for _ in range(20)
        ]
    
    def operation2(self, list: List) -> None:
        list.sort()
        print(list)
        
if __name__ == '__main__':
    c1 = ConcreteClass1()
    c2 = ConcreteClass2()
    c1.template_method()
    c2.template_method()
    
    
    
    