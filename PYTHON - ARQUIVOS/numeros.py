# Exercício 1 — Ler números de um arquivo
# Crie um arquivo chamado:
# numeros.txt
# com o conteúdo:
# 10
# 20
# 30
# 40
# 50
# Faça um programa que:
# leia todos os números do arquivo;
# calcule a soma;
# exiba o resultado.
# Saída esperada:
# Soma = 150

with open("numeros.txt", "r") as arq:
    soma = 0

    for linha in arq:
        valor = int(linha)
        soma += valor
    
    print(f"Soma das linhas: {soma}")