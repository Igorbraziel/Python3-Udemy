# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    lista_total = []
    i = 0
    
    while i < len(lista1) and i < len(lista2):
        lista_total.append((lista1[i], lista2[i]))
        i += 1    
        
    return lista_total


lista = zipper(lista1, lista2)
print(lista)
    