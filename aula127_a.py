import json


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
p1 = Pessoa("Igor", 18)
p2 = Pessoa("Nine", 19)
p3 = Pessoa("Isabela", 12)

dados = [vars(p1), vars(p2), vars(p3)]

with open("pessoa.json", "wt") as arq:
    json.dump(dados, arq, indent=2)