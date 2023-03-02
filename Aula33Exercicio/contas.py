from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, numconta: int, saldo: float = 0) -> None:
        self._agencia = agencia
        self._numconta = numconta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, dep: int) -> float:
        if isinstance(dep, int):
            self._saldo += dep
            self.detalhes(f'(DEPÓSITO R${dep:.2f})')
            return self._saldo
        else:
            raise ValueError

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._agencia!r}, {self._numconta!r}, {self._saldo!r})'
        return f'{class_name}{attrs}'

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R${self._saldo:.2f}, {msg}')
        print('=' * 50)


class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        if isinstance(valor, float):
            valor_pos_saque = self._saldo - valor

            if valor_pos_saque >= 0:
                self._saldo -= valor
                self.detalhes(f'(SAQUE R${valor:.2f})')
                return self._saldo

            print('Não foi possivel sacar o valor desejado')
            self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        else:
            raise ValueError


class ContaCorrente(Conta):
    def __init__(self, agencia, numconta, saldo=0, limite=0) -> None:
        super().__init__(agencia, numconta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        if isinstance(valor, float):
            valor_pos_saque = self._saldo - valor
            limite_maximo = -self.limite

            if valor_pos_saque >= limite_maximo:
                self._saldo -= valor
                self.detalhes(f'(SAQUE R${valor:.2f})')
                return self._saldo

            print('Não foi possivel sacar o valor desejado')
            print(f'Seu limite é {-self.limite:.2f}')
            self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        else:
            raise ValueError

        def __repr__(self) -> str:
            class_name = type(self).__name__
            attrs = f'({self._agencia!r},{self._numconta!r},{self._saldo!r})'\
                f'{self.limite!r}'
            return f'{class_name}{attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(100)
    cp1.sacar(100)

    print('#' * 50)

    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(100)
    cc1.sacar(99)
    cc1.sacar(100)
    cc1.sacar(100)

    print('#' * 50)
