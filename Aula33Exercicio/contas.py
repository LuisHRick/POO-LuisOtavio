from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numconta, saldo) -> None:
        self._agencia = agencia
        self._numconta = numconta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor): ...

    def depositar(self, dep):
        self._saldo += dep
        self.detalhes(f'(DEPÓSITO {dep})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self._saldo:.2f}, {msg}')