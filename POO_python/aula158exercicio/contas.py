from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, dinheiro: float = 0):
        self.agencia = agencia
        self.numero_conta = numero
        self.total_dinheiro = dinheiro     
        
    @abstractmethod
    def sacar(self, dinheiro) -> bool:
        ...
        
    def depositar(self, dinheiro):
        self.total_dinheiro += dinheiro
        self.detalhes(f'(DEPÓSITO DE R${dinheiro:.2f})')
        
    def detalhes(self, msg=''):
        print(f'Seu saldo é de {self.total_dinheiro}', msg)
        
    def __repr__(self):
        class_name = type(self).__name__
        class_attrs = f'({self.agencia}, {self.numero_conta}, {self.total_dinheiro})'
        return f'{class_name}{class_attrs}'
        
        
class ContaCorrente(Conta):
    def __init__(self, agencia, numero, dinheiro = 0, limite = 0):
        super().__init__(agencia, numero, dinheiro) 
        self.LIMITE = limite
        
    def sacar(self, dinheiro) -> bool:
        if self.total_dinheiro + self.LIMITE >= dinheiro:
            self.total_dinheiro -= dinheiro
            self.detalhes(f'(SAQUE DE R${dinheiro:.2f})')
            return True
        self.detalhes('(SAQUE NEGADO)')
        return False
    

class ContaPoupanca(Conta):
    def sacar(self, dinheiro) -> bool:
        if self.total_dinheiro >= dinheiro:
            self.total_dinheiro -= dinheiro
            self.detalhes(f'(SAQUE DE R${dinheiro:.2f})')
            return True
        self.detalhes('(SAQUE NEGADO)')
        return False
    
    
if __name__ == '__main__':
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(100)