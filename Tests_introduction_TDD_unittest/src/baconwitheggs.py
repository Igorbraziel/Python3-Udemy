"""
1 - Receber um número inteiro
2 - Saber se o número é multiplo de 3 e 5:
    Bacon com ovos
3 - Saber se o número NÃO é multiplo de 3 e 5:
    Passa fome
4 - Saber se o número é multiplo somente de 3:
    Bacon
5 - Saber se o número é multiplo somente de 5:
    Ovos
"""

def bacon_with_eggs(n):
    assert isinstance(n, int), 'n must be int'
    
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon With Eggs'
    
    if n % 3 == 0:
        return 'Bacon'
    
    if n % 5 == 0:
        return 'Eggs'
    
    return 'Starve'