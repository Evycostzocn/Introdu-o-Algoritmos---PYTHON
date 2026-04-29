"""
Peça ao usuário um número inteiro positivo N.
Desenvolva um programa que imprima uma sequência de linhas formando uma escada numérica crescente, iniciando em 1 e indo até N, de forma que cada linha
contenha os números de 1 até o valor da linha.
Em seguida, o programa deve imprimir a escada inversa, reduzindo progressivamente
até 1.
Exemplo (N = 4):
1
12
123
1234
123
12
1
"""
n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()