# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class ClassError(Exception):
    ...

class OutroErro(Exception):
    ...

def levantar():
    exception_ = ClassError('A mensagem do meu erro')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    levantar()
except ClassError as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OutroErro('Vou lançar de novo')
    raise exception_ from error