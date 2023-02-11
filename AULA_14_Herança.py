# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    cpf = 'CPF PESSOA'

    def falar(self):
        print(self.nome, self.sobrenome ,self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    cpf = 'CPF ALUNO'

c1 = Cliente('Luis', 'Fernando')
a1 = Aluno('Maria', 'Clara')

c1.falar()
print(c1.cpf)

a1.falar()
print(a1.cpf)