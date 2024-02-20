class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def mostrar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__, sep=' ')
        
class Cliente(Pessoa):
    ...#está herdando de Pessoa
    
class Aluno(Pessoa):
    ...#está herdando de Pessoa
    
c1 = Cliente("Igor", "Braziel")
a1 = Aluno("Nine", "Araujo")
c1.mostrar_nome_classe()
a1.mostrar_nome_classe()