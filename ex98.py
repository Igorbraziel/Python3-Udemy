import re

cpf = input("CPF [048.777.271-75]: ").strip()
numeros = []
soma = k = 0
valido = True

new_cpf = re.sub(fr'[^0-{len(cpf)}]', '', cpf)

if new_cpf.count(new_cpf[0]) == len(new_cpf):
    valido = False

for i, item in enumerate(cpf):
    try:
        numeros.append(int(item)) #vejo se o item escolhido é um numero e adiciona na minha lista
    except:
        continue

for i in range(10, 1, -1):
    soma += i * numeros[k] # multiplio os primeiros nove números do cpf por 10 até 2 respectivamente
    k += 1

soma *= 10 #multiplico minha soma por 10
resto = soma % 11

if resto > 9:
    resto = 0

if resto != numeros[9]:
    valido = False # verifico se o digito é igual ao resto

# daqui pra baixo confiro o ultimo digito

soma = 0
k = 0
resto = 0

for i in range(11, 1, -1):
    soma += i * numeros[k] # somo meus numeros até o penultimo, multiplicando de 11 até 2
    k += 1

soma *= 10 #multiplico minha soma por 10

resto = soma % 11

if resto > 9:
    resto = 0

if resto != numeros[-1]:
    valido = False # verifico se o digito é igual ao resto

if valido:
    print(f'O CPF {cpf} é valido')
else:
    print(f"O CPF {cpf} é inválido")

