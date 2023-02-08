import json

caminho_arquivo = 'aula4.json'

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = pessoa('joão', 13)
pessoa2 = pessoa('fernanda', 27)
pessoa3 = pessoa('mariana', 18)
pessoas_arquivadas = [vars(pessoa1), vars(pessoa2), vars(pessoa3)]

def adiar():
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(pessoas_arquivadas, arquivo, indent= 2, ensure_ascii= False)

if __name__ == '__main__':
    adiar()