
# ATRIBUTOS QUE COMEÇAM COM 1 OU 2 UNDERLINES ( _ ) NÃO DEVEM SER USADOS FORA DA CLASSE

# Getter -> Obter valor
# Setter -> Armazenar e alterar valor

# O getter e o setter podem e devem ter o mesmo nome, pois só será executado o devido para aquela ocasião.
# Como o setter server para alterar um valor após usar um Getter, é possível iniciar o método sem pedir 
# um parâmetro para aquela variável.
class Caneta:
    def __init__(self, cor):
        # _protected
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('GETTER')
        return self._cor
    
    # Decorator Setter, usar o formato   Nome.Setter
    @cor.setter
    def cor(self, valor):
        print('SETTER')
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
print(caneta.cor)

caneta.cor = 'Rosa'
print(caneta.cor)

print(caneta.cor_tampa)

caneta.cor_tampa = 'Verde'
print(caneta.cor_tampa)