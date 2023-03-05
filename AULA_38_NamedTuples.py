# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
import typing
from collections import namedtuple

carta = namedtuple(
    'Carta', ['valor', 'naipe'],
    defaults=['Valor', 'Naipe']
)
as_espadas = carta('A', 'Espadas')
print(as_espadas)
print(as_espadas.naipe)
print(as_espadas.valor)


class Carta(typing.NamedTuple):
    valor: str = 'Valor'
    naipe: str = 'Naipe'