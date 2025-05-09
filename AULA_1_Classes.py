# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = pessoa('Lucas', 'Felipe')

p2 = pessoa('Maria', 'Helena')

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)