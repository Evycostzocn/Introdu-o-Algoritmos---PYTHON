"""
Exercício 1 Fatorial de um número
Escreva um programa que leia um número inteiro positivo n e calcule o seu fatorial.

Lembre-se de que:

n! = n × (n-1) × (n-2) × ... × 1
Exemplo:

5! = 5 × 4 × 3 × 2 × 1 = 120
Saída esperada:

Digite um número: 5
Fatorial: 120
"""

n = int(input("digite um número: "))
fatorial = 1

for i in range(1, n + 1, n - 1):
    fatorial *= n
print(fatorial)