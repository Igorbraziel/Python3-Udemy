from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self):
        self._data = dict()
        self._index = 0
        self._next_index = 0
        
    def __len__(self) -> int:
        return self._index
        
    def append(self, value):
        self._data[self._index] = value
        self._index += 1
        
    def __iter__(self):
        return self
    
    def __getitem__(self, index):
        if index < self.__len__():
            return self._data[index]
        
    def __setitem__(self, index, value):
        self._data[index] = value
        
    def __next__(self):
        if self._next_index >= self.__len__():
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value
            


if __name__ == '__main__':
    lista = MyList()
    lista.append('Igor')
    for item in lista:
        print(item)
        
    lista.append('nine')
    lista.append('isabela')
    lista.append('nine')
    #lista[3] = 'ultimo'
        
    for item in lista:
        print(item)