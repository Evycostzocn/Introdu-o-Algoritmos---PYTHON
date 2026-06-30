# Exercício 2 — Contador de linhas
# Crie uma função:
# contar_linhas(nome_arquivo)
# que receba o nome de um arquivo e retorne quantas linhas ele possui.
# Teste usando:
# frases.txt
# com algumas frases.

def contar_linhas(nome_arquivo):
    countLinha = 0
    with open(nome_arquivo, "r") as arq:
        for linha in arq:
            countLinha += 1
    return countLinha

arquivo = "frases.txt"

numLinhas = contar_linhas(arquivo)

print(f"Numero de linhas: {numLinhas}")

