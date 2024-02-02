import copy
arq = open("aula116.txt", "at")

pessoas = list()
dados = dict()

qtd = int(input("Digite a quantidade de entradas: "))

for i in range(0, qtd):
    dados["nome"] = str(input("Digite seu nome: "))
    dados["idade"] = int(input("Digite a sua idade: "))
    pessoas.append(copy.deepcopy(dados))
    dados.clear()
    
for pessoa in pessoas:
    for key, value in pessoa.items():
        arq.write(f"{key.capitalize()}: {value.capitalize() if isinstance(value, str) else value}\n")
        
arq.close()

leitura = open("aula116.txt", "rt")

print(leitura.read())
    