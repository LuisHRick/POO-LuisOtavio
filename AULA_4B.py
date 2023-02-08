from AULA_4_JsonClass import caminho_arquivo, pessoa
import json

with open(caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)

    p1 = pessoa(**dados[0])
    p2 = pessoa(**dados[1])
    p3 = pessoa(**dados[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)