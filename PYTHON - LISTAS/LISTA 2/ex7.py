"""
Em análise de imagens, um filtro de suavização substitui o valor de um pixel pela
média dele e de seus vizinhos diretos (cima, baixo, esquerda, direita). Dada uma
matriz de inteiros N × N, aplique esse filtro a todos os elementos internos (excluindo
as bordas) e imprima a nova matriz.
"""

n = int(input("n: "))
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        preenche_matriz = int(input("Digite os valores iniciais para preencher a matriz: "))
        linha.append(preenche_matriz)
    matriz.append(linha)

nova_matriz = [linha[:] for linha in matriz]


for i in range(1, n - 1):
    for j in range(1, n - 1):
        soma = ( 
            matriz[i][j - 1] 
            + matriz[i][j + 1] 
            + matriz[i][j]
            + matriz[i - 1][j]
            + matriz[i + 1][j]
        )
        media = soma / 5

        nova_matriz[i][j] = media

for linha in nova_matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

    