"""
 Um mapa de jogo é representado por uma matriz J de dimensão N × M onde cada
célula possui uma pontuação. O jogador começa em J[0][0] e só pode se mover para
a direita ou para baixo. Escreva uma função que calcule a maior pontuação possível
que o jogador pode coletar ao chegar em J[N − 1][M − 1].
"""


n = int(input("linhas: "))
m = int(input("colunas: "))

matriz = []

for i in range(n):
    linhas = []
    for j in range(m):
        pontos = int(input("valor: "))
        linhas.append(pontos)
    matriz.append(linhas)

for j in range(1, len(matriz[0])):
    matriz[0][j] += matriz[0][j - 1]

for i in range(1, len(matriz)):
    matriz[i][0] += matriz[i - 1][0]

for i in range(1, len(matriz)):
    for j in range(1, len(matriz[i])):
        matriz[i][j] += max(
            matriz[i - 1][j],
            matriz[i][j - 1]
        )

print(matriz[-1][-1])


