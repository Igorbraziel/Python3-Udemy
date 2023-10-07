import os
compras = []
while True:    
    print("Selecione uma opção:")
    op = input("[i]nserir [a]pagar [l]istar: ").lower().strip()[0]
    if op not in 'ial':
        print('Opção inválida')
        os.system("clear")
        continue
    if op == 'l':
        if len(compras) == 0:
            print('Não há itens para listar')
            os.system("clear")
        else:
            for indice, itens in enumerate(compras):
                print(f'{indice} - {itens}')
    elif op == 'i':
        compras.append(input("Valor: "))
    elif op == 'a':
        indice = int(input("Digite um indice para apagar: "))
        if 0 <= indice < len(compras):
            compras.pop(indice)
        else:
            print("Indice invalido!")
            os.system("clear")
