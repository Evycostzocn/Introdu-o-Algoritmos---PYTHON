"""
Considere a série:
S =  1 · 1 / 1! + (1 + 2) · (1 · 2) / 2! + (1 + 2 + 3) · (1 · 2 · 3) / 3! + (1 + 2 + 3 + 4) · (1 · 2 · 3 · 4) / 4! +· · · 
Escreva um programa que leia um valor inteiro n e calcule os n primeiros termos
dessa série e sua soma final.
"""

"""
n = int(input("n: "))
total = 0
soma = 0
produto = 1
fatorial = 1
i = 1

while i <= n:
    soma += i
    produto *= i
    fatorial *= i

    termo = (soma * produto) / fatorial
    print(f"termo {i} = {termo}")
    total += termo
    i += 1
print(f"soma total: {total:.2f}")
"""

n = int(input("n: "))
soma = 0
total = 0

for i in range(1, n + 1):
    soma += i
    termo = soma
    print(f"termo {i} = {termo}")
    total += termo
print(f"soma total = {total:.2f}")
