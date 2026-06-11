"""
Desenvolva um programa que leia uma matriz de dimensões M × N e gere a sua
matriz transposta (N×M). Crie uma função específica transpor(M) para realizar
esta operação, retornando a nova estrutura sem alterar a original.
"""

def transpor(matriz):
    nova_matriz = []
    for i in range(len(matriz[0])):
        linhas_transpostas = []
        for j in range(len(matriz)):
            linhas_transpostas.append(matriz[j][i])
        nova_matriz.append(linhas_transpostas)
    return nova_matriz

m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))

matriz = []

for i in range(m):
    linhas = []
    for j in range(n):
        pontos = int(input("Digite o valor do ponto: "))
        linhas.append(pontos)
    matriz.append(linhas)

nova_matriz = transpor(matriz)
for linha in nova_matriz:
    print(linha)