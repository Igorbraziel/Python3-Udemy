def funcao():
    def multiplicar(numero, multiplicador):
        return numero * multiplicador
    return multiplicar

num = int(input("Número: "))

numero = funcao()

print(numero(num, 2))
print(numero(num, 3))
print(numero(num, 4))