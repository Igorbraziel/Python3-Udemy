import json
from aula127_a import Pessoa


with open("pessoa.json", "rt") as arq:
    lista = json.load(arq)
    
p1 = Pessoa(**lista[0])
p2 = Pessoa(**lista[1])
p3 = Pessoa(**lista[2])

print(*lista, sep="\n")
print(p1.nome)
print(p1.idade)
print(p2.nome)
print(p2.idade)
print(p3.nome)
print(p3.idade)


