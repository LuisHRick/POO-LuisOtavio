import contas
import pessoas


class Banco():
    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes_registrados: pessoas.Cliente | None = None,
                 contas_registradas: contas.Conta | None = None,
                 ) -> None:
        self.conta = contas_registradas or []
        self.agencias = agencias or []
        self.clientes = clientes_registrados or []

    def _checa_agencia(self, conta_checagem):
        if conta_checagem.agencia not in self.agencias:
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

    def autenticar(self, cliente, conta):
        ...
