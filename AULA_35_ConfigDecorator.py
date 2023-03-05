from dataclasses import dataclass


# Existem configurações para essa classe que fazem coisas interessantes, como os
# Frozen, Init, Reverse, Repr...
@dataclass(frozen=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == "__main__":
    nome = Pessoa('Luiz', 'Otavio')
    print(nome)
