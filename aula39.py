nome = input('Digite o seu nome: ')
nova_string = ''
i = 0
k = 0
while i < len(nome):
    if i == 0:
        nova_string += '*'
    nova_string += nome[i]
    nova_string += '*'

    i += 1
print(nova_string)
