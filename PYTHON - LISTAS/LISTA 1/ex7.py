"""
Considere a série:
S =  2 / 1^2 + 2 · 3 / 2^2  + 2 · 3 · 4 / 3^2 + 2 · 3 · 4 · 5 / 4^2 + · · · 
Escreva um programa que leia um valor inteiro n e calcule os n primeiros termos
dessa série e sua soma final.
Observação: o numerador de cada termo é formado por um produtório sequencial
começando em 2, e o denominador é o quadrado da posição do termo.
"""

n = int(input("n: "))
numerador = 1
soma = 0

for i in range (1, n + 1):
    numerador *= (i + 1)
    termo = numerador / (i ** 2)
    soma += termo
print(f"resultado: {soma:.2f}")