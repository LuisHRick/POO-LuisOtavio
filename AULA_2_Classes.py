class carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = carro('fusca')
print(fusca.nome)
fusca.acelerar()

celta = carro('celta')
print(celta.nome)
celta.acelerar()