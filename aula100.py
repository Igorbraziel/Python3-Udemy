import copy
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

def ordena_nome(dicionario):
    return dicionario["nome"]


def ordena_preco(dicionario):
    return dicionario["preco"]

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = []
produtos_ordenados_nome = []
produtos_ordenados_preco = []
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

for produto in produtos:
    produto["preco"] = round(produto["preco"] + ((10/100) * produto["preco"]), 2)
    novos_produtos.append(copy.deepcopy(produto))
    
novos_produtos.sort(key=ordena_nome, reverse=True)

for produto in novos_produtos:
    produtos_ordenados_nome.append(copy.deepcopy(produto))
    
novos_produtos.sort(key=ordena_preco, reverse=False)

for produto in novos_produtos:
    produtos_ordenados_preco.append(copy.deepcopy(produto))
    

print("=" * 60)    
print(*produtos_ordenados_nome, sep="\n")
print("=" * 60)
print(*produtos_ordenados_preco, sep="\n")
print("=" * 60)

