# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A(object):

    def __new__(cls, x):
        return super().__new__(cls)

    def __init__(self, x):
        self.x = x
        print(self)

    def __repr__(self) -> str:
        return 'A()'

a = A()