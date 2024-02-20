class Multiplicar:
    def __init__(self, func):
        self._func = func
        
    def __call__(self, *args, **kwargs):
        resultado = self._func(*args)
        return resultado * 10
    
    
@Multiplicar
def soma(x, y):
    return x + y


dois_mais_sete = soma(2, 7)
print(dois_mais_sete)