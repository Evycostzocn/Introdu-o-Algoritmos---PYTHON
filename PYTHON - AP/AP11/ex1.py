"""
Exercício 1 Montando uma matriz pequena
Crie um programa em Python que leia os valores de uma matriz de 2 linhas e 3 colunas.

O programa deve exibir a matriz completa, linha por linha.

Exemplo de entrada
1
2
3
4
5
6
Saída esperada
[1, 2, 3]
[4, 5, 6]
"""

matriz = []

for i in range(2):
    linha = []
    for j in range (3):
        valor = int(input("valor: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)