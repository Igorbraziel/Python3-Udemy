from log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
            
class SmartPhone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()
        if self._ligado:
            self.log_success(f'Seu {self._nome} está ligado')
        
    def desligar(self):
        super().desligar()
        if not self._ligado:
            self.log_error(f'Seu {self._nome} está desligado')