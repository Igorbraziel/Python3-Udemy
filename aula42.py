frase = 'O Python é uma linguagem de programação' \
        'multiparadigma' \
        'Python foi criado por Guido Van Rossum'.lower().strip()

for indice, letra in enumerate(frase):
    if indice == 0:
        letra_atual = letra
    elif frase.count(letra) > frase.count(letra_atual) and letra != ' ':
        letra_atual = letra
print(f'A letra que apareceu mais vezes foi ({letra_atual.upper()})')
print(f'Ela apareceu {frase.count(letra_atual)} vezes')
