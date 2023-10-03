nome = str(input('Digite o seu nome: '))

if len(nome) > 1:
    if len(nome) <= 4:
        print('Seu nome é pequeno')
    elif 5 <= len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Nome inválido')
