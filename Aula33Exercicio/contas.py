from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numconta, saldo) -> None:
        self._agencia = agencia
        self._numconta = numconta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor): ...

    def depositar(self, dep: int):
        if isinstance(dep, int):
            self._saldo += dep
            self.detalhes(f'(DEPÓSITO R${dep:.2f})')
        else:
            raise ValueError


    def detalhes(self, msg=''):
        print(f'O seu saldo é R${self._saldo:.2f}, {msg}')
        print('=' * 50)

class ContaPoupanca(Conta):
    def __init__(self, agencia, numconta, saldo) -> None:
        super().__init__(agencia, numconta, saldo)
    
    def sacar(self, valor: int):
        if isinstance(valor, int):
            valor_pos_saque = self._saldo - valor
            
            if valor_pos_saque >= 0:
                self._saldo -= valor
                self.detalhes(f'(SAQUE R${valor:.2f})')
                return self._saldo
            
            print('Não foi possivel sacar o valor desejado')
            self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        else:
            raise ValueError




if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)