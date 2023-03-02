class Pessoa():
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome


if __name__ == '__main__':
    p1 = Pessoa('Jonas', 31)
    print(p1.nome)
    print(p1.idade)
