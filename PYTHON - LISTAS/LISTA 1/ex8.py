"""
Considere a série: S = 1 / 2 · 1 + 1 · 3 / 2^2 · 2 + 1 · 3 · 5 / 2^3 · 3 + 1 · 3 · 5 · 7 / 2^4 · 4 + · · · 
Escreva um programa que leia um valor inteiro n e calcule os n primeiros termos dessa série e sua soma final.
"""

n = int(input("n: "))
numerador = 1
soma = 0

for i in range(1, n + 1):
    numerador *= (2 * i - 1)
    termo = numerador / ((2 ** i) * i)
    soma += termo
print(f"resultado: {soma:.2f}")
