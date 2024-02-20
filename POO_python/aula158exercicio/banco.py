import contas
import pessoas


class Banco:
    def __init__(self, 
                 agencias_: list[int] | None = None,
                 clientes_: list[pessoas.Cliente] | None = None, 
                 contas_: list[contas.Conta] | None = None
                 ):
        self._agencias = agencias_ or []
        self._clientes = clientes_ or []
        self._contas = contas_ or []
    
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        
    def checa_agencia(self, agencia) -> bool:
        if agencia in self._agencias:
            return True
        return False
                    
    def checa_conta(self, conta) -> bool:
        if conta in self._contas:
            return True
        return False
        
    def checa_cliente(self, cliente) -> bool:
        if cliente in self._clientes:
            return True
        return False
        
        
    def autenticar(self, cliente: pessoas.Cliente):
        if self.checa_cliente(cliente) and self.checa_conta(cliente.conta) and self.checa_agencia(cliente.conta.agencia):
            return True
        return False
    
    def __repr__(self):
        class_name = self.__class__.__name__
        class_attrs = f'({self._agencias}, {self._clientes}, {self._contas})'
        return f'{class_name}{class_attrs}'
    
if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco._clientes.extend([c1, c2])
    banco._contas.extend([cc1, cp1])
    banco._agencias.extend([cc1.agencia, cp1.agencia])

    if banco.autenticar(c2):
        cp1.depositar(10)
        c2.conta.depositar(100)
        print(c2.conta)
    