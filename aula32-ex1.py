num = input('Digite um número inteiro: ')

if num.isnumeric():
    num = int(num)
    num = num.__trunc__()
    if num % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é ímpar')
else:
    print(f'({num}) não é um número inteiro')