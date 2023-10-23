# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
import itertools


def combinacao2(lista):
    combina = []
    for i in range(0, len(lista)):
        for j in range(i + 1, len(lista)):
            combina.append((lista[i], lista[j]))
    return combina


def permutation2(lista):
    permut = []
    for item1 in lista:
        for item2 in lista:
            if item1 != item2:
                permut.append((item1, item2))   
    return permut


def product4(*lista):
    produtos = []
    for c1 in range(0, len(lista[0])):
        for c2 in range(0, len(lista[1])):
            for c3 in range(0, len(lista[2])):
                for c4 in range(0, len(lista[3])):
                    produtos.append((lista[0][c1], lista[1][c2], lista[2][c3], lista[3][c4]))
    return produtos


def print_lista(lista):
    print("=-" * 30)
    print(*lista, sep="\n")
    print("=-" * 30)        

#def print_iter(iterator):
#    print(*list(iterator), sep='\n')
#    print()
#
#
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

#pessoas_combina = list(itertools.combinations(pessoas, 2))
#print_lista(pessoas_combina)
#
#pessoas_permut = list(itertools.permutations(pessoas, 2))
#print_lista(pessoas_permut)



camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

camisetas_produtos = itertools.product(*camisetas)
print_lista(camisetas_produtos)
#print_iter(combinations(pessoas, 2))
#print_iter(permutations(pessoas, 2))
#print_iter(product(*camisetas))