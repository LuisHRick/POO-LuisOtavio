# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        return 'método público'

    def _metodo_protegido(self):
        return 'método protegido'

    def __metodo_privado(self):
        return 'método privado'

f = foo()
print(f.public)
print(f.metodo_publico())

print(f._protected)           # -> Errado
print(f._metodo_protegido())  # -> Errado


# O nome do método foi alterado por ser um método privado, só será o original dentro da classe original
print(f.__private)            # -> Errado
print(f.__metodo_privado())   # -> Errado