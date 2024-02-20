from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        
    @abstractmethod
    def enviar(self) -> bool:
        ...
        

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS enviado:', self.mensagem)
        return True
    
    
class NotificacaoEMAIL(Notificacao):
    def enviar(self) -> bool:
        print('E-MAIL enviado:', self.mensagem)
        return True
    
    
def notificar(notificacao: Notificacao):
    retorno = notificacao.enviar()
    
    if retorno:
        print('Deu certo')
    else:
        print('Deu errado')
        
        
sms = NotificacaoSMS('testando SMS')
email = NotificacaoEMAIL('testando email')
notificar(sms)
notificar(email)
