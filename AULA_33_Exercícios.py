"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
"""
class Conta():
    def __init__(self, agencia, numconta, saldo) -> None:
        self._agencia = agencia
        self._numconta = numconta
        self._saldo = saldo

    def deposito(self, dep):
        self._saldo += dep

class ContaCorrente(Conta):
    ...

class ContaPoupanca(Conta):
    ...

class Pessoa():
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Cliente(Pessoa):
    def __init__(self) -> None:
        self.conta = ...

class Banco():
    def __init__(self) -> None:
        self._contas = []
        self._clientes = []


