soma = 0
num = 1
div = 2
valor = True
while div < 1000000:
    try:
        soma += num/div
        div *= 2
    except:
        valor = False
print(f'A soma é {soma} e o número é {num}/{div}')