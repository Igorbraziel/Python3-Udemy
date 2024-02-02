#class method + factories(fabricas)

class Pessoa:
    def __init__(self, nome, idade, qualidade):
        self.nome = nome
        self.idade = idade
        self.qualidade = qualidade
        
    @classmethod
    def criar_com_50_anos(cls, nome, qualidade):
        return cls(nome, 50, qualidade)
    
    @classmethod
    def bonito_com_20(cls, nome):
        return cls(nome, 20, "bonito")
        
        
eu = Pessoa("Igor", 18, "cheiroso")
nine = Pessoa.bonito_com_20("Nine")
isabela = Pessoa.criar_com_50_anos("isabela", "chorona")

print(vars(eu))
print(nine.__dict__)
print(isabela.__dict__)
