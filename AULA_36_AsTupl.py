from dataclasses import asdict, astuple, dataclass


@dataclass(frozen=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == "__main__":
    nome = Pessoa('Luiz', 'Otavio')
    print(nome)
    print(asdict(nome))
    print(astuple(nome))
