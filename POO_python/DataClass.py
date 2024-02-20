from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float
    
if __name__ == '__main__':
    lista = [Pessoa('igor', 19, 1.75), Pessoa('nine', 19, 1.62), Pessoa('isabela', 12, 1.5)]
    lista.sort(key=lambda pessoa: pessoa.altura)
    print(lista)