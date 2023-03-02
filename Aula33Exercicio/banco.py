import contas
import pessoas


class Banco():
    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes_registrados: list[pessoas.Cliente] | None = None,
                 contas_registradas: list[contas.Conta] | None = None,
                 ) -> None:
        self.conta = contas_registradas or []
        self.agencias = agencias or []
        self.clientes = clientes_registrados or []

    def _checa_agencia(self, conta_checagem):
        if conta_checagem.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente_checagem):
        if cliente_checagem in self.clientes:
            return True
        return False

    def _checa_conta(self, conta_checagem):
        if conta_checagem in self.conta:
            return True
        return False

    def _checa_conta_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_conta_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.clientes!r},{self.agencias!r},{self.conta!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.conta.extend([cc1, cp1])
    banco.agencias.extend([111, 112])
    print(banco)

    print(banco.autenticar(c1, cc1))
