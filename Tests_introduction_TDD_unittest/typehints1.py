from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence

#Primitives
number: int = 10
floating: float = 11.5
boolean: bool = False
string: str = 'Igor'

#Sequences
list_: list = [1, '3', True]
variable_list: List[Union[int, str]] = [1, 'Hello']
tuple_: Tuple[int, int, int, str] = (1, 2, 3, 'String')

#Dict
person: Dict[str, Union[int, str]] = {'name': 'Igor', 'agr': 20}
any_: Any = [1, 'Hi', False]

#Alias
MyDict = Dict[str, List[Union[bool, int]]]
my_dict: MyDict = {'list': [True, False, 10, 20]}

#NewType
UserId = NewType('UserId', int)
user_id = UserId(257)

def return_function(function: Callable[[], None]) -> Callable:
    return function

def say_hello():
    print('Hello!')
    
return_function(say_hello)()

def iterator_function(sequence: Sequence):
    return [x * 2 for x in sequence]

print(iterator_function([1, 2, 3]))
print(iterator_function(['1', '2', '3']))
print(iterator_function((1, '2', 3)))




