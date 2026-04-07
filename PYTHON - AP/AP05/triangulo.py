"""
Exercício 13 Triângulo crescente de números
Leia um número inteiro positivo n e mostre um triângulo de números.

Para n = 5, a saída deve ser:

1
12
123
1234
12345
"""

n = int(input("digite um número: "))

for i in range (1, n + 1):
    for j in range (1, i + 1):
        print(j, end="")
    print()
