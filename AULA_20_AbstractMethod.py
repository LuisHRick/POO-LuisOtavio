# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):  # type: ignore
        self.name = name
        self._name = None

        @property
        def name(self):
            return self._name

        @name.setter
        @abstractmethod
        def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, nome):
        super().__init__(nome)

    @AbstractFoo.name.setter  # type: ignore
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)
