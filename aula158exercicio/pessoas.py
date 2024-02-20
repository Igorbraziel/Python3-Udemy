import contas

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade
        
    def __repr__(self):
        class_name = type(self).__name__
        class_attrs = f'({self._nome}, {self._idade})'
        return f'{class_name}{class_attrs}'
        
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
    
    def adicionar_conta(self, conta):
        self.conta = conta  
    
if __name__ == '__main__':
    c1 = Cliente('Igor', 19)
    c1.adicionar_conta(contas.ContaPoupanca(123, 234, 789))
    print(c1)
    print(c1.conta)