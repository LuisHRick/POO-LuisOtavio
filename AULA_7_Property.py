# Um método Get só que melhor
# Para que serve:
# - como getter
# - para evitar quebrar código cliente
# - para habilitar setter
# - para executar funções ao obter um atributo

# Código cliente é o código q usa o seu código

# Sem o decorator @property:
'''
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    def get_cor(self):
        print('Get Cor')
        return self.cor_tinta


caneta = Caneta('Azul')
print(caneta.get_cor())

'''

# Com o decorator @property

class Caneta:
    def __init__(self, cor, tampa='Preta'):
        self.cor_tinta = cor
        self.tampa = tampa

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta


    @property
    def cor_tampa(self):
        print('PROPERTY 2')
        return self.tampa

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)