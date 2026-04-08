"""
Exercício 15 Soma harmônica simples
Escreva um programa que leia um número inteiro positivo n e calcule a soma:

S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Ao final, mostre o valor de S.

Este exercício é um primeiro passo para trabalhar séries com frações utilizando repetição com while.
"""

"""n = int(input("n: "))
soma = 0
count = 1

for i in range(1, n + 1):
    soma += 1 / i
print(f"{soma:.2}")
"""

n = int(input("n: "))
soma = 0
i = 1
while i <= n:
    soma += 1 / i
    i += 1
print(f"{soma:.2f}") 