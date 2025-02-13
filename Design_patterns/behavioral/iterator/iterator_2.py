from collections.abc import Iterator, Iterable
from typing import List, Any

class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1
        
    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration
    
    
class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        
    def add(self, value: Any) -> None:
        self._items.append(value)
        
    def __iter__(self) -> Iterator:
        return ReverseIterator(self._items)
    
    
if __name__ == '__main__':
    my_list = MyList()
    my_list.add('Igor')
    my_list.add('Nine')
    my_list.add(22)
    my_list.add(True)
    
    for value in my_list:
        print(value)
        