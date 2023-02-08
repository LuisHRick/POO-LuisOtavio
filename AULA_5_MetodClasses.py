class pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod                                      # Faz eu executar a função sem ter que passar nada como parâmetro
    def metodo_de_classe(cls):
        print('hey')

    @classmethod
    def criar_com_50(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('anônima', idade)

pessoa_1 = pessoa.criar_sem_nome(23)
print(pessoa_1.nome, pessoa_1.idade)

pessoa_2 = pessoa.criar_com_50('Helena')
print(pessoa_2.nome, pessoa_2.idade)

pessoa.metodo_de_classe()
