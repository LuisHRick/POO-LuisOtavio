# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod


class Notificação(ABC):
    def __init__(self, mensagem) -> None:
        self._mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificaçãoEmail(Notificação):
    def enviar(self) -> bool:
        print('E-mail: enviando: ', self._mensagem)
        return True


class NotificaçãoSMS(Notificação):
    def enviar(self) -> bool:
        print('SMS: enviando: ', self._mensagem)
        return True


def notificar(notificacao: Notificação):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('notificação enviada')
    else:
        print('Notificação não enviada')


mensagem_sms = NotificaçãoSMS('Mensagem Teste -> SMS')
notificar(mensagem_sms)

mensagem_Email = NotificaçãoEmail('Mensagem Teste -> E-mail')
notificar(mensagem_Email)

# msg = NotificaçãoSMS('Testando notificação')
# msg.enviar()
