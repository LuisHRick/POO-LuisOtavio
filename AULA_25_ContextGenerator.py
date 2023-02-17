from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(caminho_arquivo, modo)
        yield arquivo
    except Exception as e:
        print(e)
    finally:
        print('fechando arquivo')
        arquivo.close()

with my_open('aula25', 'w') as arquivo:
    arquivo.write('Linha 1')
    arquivo.write('Linha 2')
    arquivo.write('Linha 3')