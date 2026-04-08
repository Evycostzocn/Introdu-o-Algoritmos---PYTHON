"""
Exercício 16 Soma com sinais alternados
Escreva um programa que leia um número inteiro positivo n e calcule a soma:

S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ... 
usando os n primeiros termos da sequência.

Este exercício é mais desafiador porque exige, além da repetição com while, o uso de uma estratégia para alternar o sinal de cada termo da soma.
"""

"""n = int(input("n: "))
soma = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        soma += 1 / i
    else:
        soma -= 1 / i
print(f"{soma:.2f}")
"""
n = int(input("n: "))
soma = 0
i = 1

while i <= n:
    if i % 2 == 1:
        soma += 1 / i
    else:
        soma -= 1 / i
    i += 1
print(f"{soma:.2f}")