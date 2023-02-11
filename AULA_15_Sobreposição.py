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

'''
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        return super().upper() 

string = MinhaString('Lalaland')

print(string.upper())
'''

class A:
    atributoA = 'valor'
    def metodo(self):
        print('A') 

class B(A):
    atributoB = 'valor'
    def metodo(self):
        super().metodo()
        print('B')

class C(B):
    atributoC = 'valor'
    def metodo(self):
        super().metodo()
        print('C')

c = C()

print(c.atributoA)
print(c.atributoB)
print(c.atributoC)

c.metodo()