import os
secret = 'perfume'
tot_tent = ''
k = i = 0
while True:
    while True:
        letra = input('Digite uma letra: ')

        k += 1

        if len(letra) == 1 and letra.isalpha():
            break
        else:
            print(f'Palavra secreta:', end = ' ')

            for l in secret:
                if l in tot_tent:
                    print(l, end = '')
                else:
                    print('*', end = '')
            print()

    if letra in secret and letra not in tot_tent:
        i = 0
        while i < secret.count(letra):
            tot_tent += letra
            i += 1

    if len(tot_tent) == len(secret):
        print('PARABÉNS VOCÊ GANHOU')
        print(f'A palavra secreta era {secret.upper()}')
        print(f'Você precisou de {k} tentativas para acertar')
        k = 0
        tot_tent = ''

    print(f'Palavra secreta:', end = ' ')

    for l in secret:
        if l in tot_tent:
            print(l, end = '')
        else:
            print('*', end = '')
    print()
    