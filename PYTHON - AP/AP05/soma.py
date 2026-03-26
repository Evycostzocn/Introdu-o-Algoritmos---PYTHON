"""
Exercício 3 Soma de 1 até n
Escreva um programa que leia um número inteiro positivo n e calcule a soma dos números de 1 até n.

Exemplo: se o usuário digitar 5, o programa deverá calcular:

1 + 2 + 3 + 4 + 5
e mostrar o resultado final.
"""

numero = int (input("digite um número: "))
soma = 0

for i in range (1, numero + 1):
    soma += i
print(soma)
