# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# Super retorna a classe Superior a aquela classe, a qual pertence a herança se houver uma.

'''
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        return super().upper() 

string = MinhaString('Lalaland')

print(string.upper())
'''

class A:

    def __init__(self, atributo) -> None:
        self.atributoA = atributo
        

    
    def metodo(self):
        print('A') 

# Adicionando mais atributos dentro de __init__ em uma classe filha.
# Para isso, é preciso que seja passado as informações requisitadas pelo INIT 
# da classe anterior (A) usando o seguinte comando:

class B(A):
    
    def __init__(self, atributo, qualquer) -> None:
        super().__init__(atributo)                    # <----

        # Agora é possível a adição de um novo atributo

        self.atributoB = qualquer

    def metodo(self):
        super().metodo()
        print('B')


# Para o primeiro parâmetro dentro de B, por padrão, será a própria
# classe e self, retornando a função da classe mão da classe dada como
# parâmetro. 
# Se o parâmetro for alterado para outra classe, então, ele retornará da 
# classe mãe da classe colocada como parâmetro.
#    Exemplo: padrao: C -> B      B -> A       SUPER() / SUPER(C, SELF)
# parâmetro alterado: C -> A                   SUPER(B, SELF)

class C(B):
    
    def __init__(self, atributo, qualquer, outro) -> None:
        super().__init__(atributo, qualquer)
        self.atributoC = outro

    def metodo(self):
        super().metodo()           # B
        super(B, self).metodo()    # A
        print('C')

c = C('Atributo 1', 'Atributo 2', 'Atributo 3')

print(c.atributoA)
print(c.atributoB)
print(c.atributoC)

c.metodo()