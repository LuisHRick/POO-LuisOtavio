# Classes decoradoras

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicar = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicar
        return interna


@Multiplicar(10)         # Depois de somar, vai multiplicar o resultado pelo parâmetro
def soma(x, y):
    return x + y


dois = soma(2, 2)
print(dois)