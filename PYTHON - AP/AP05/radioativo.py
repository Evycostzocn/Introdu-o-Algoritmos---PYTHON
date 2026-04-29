"""
Exercício 14 Monitoramento de material radioativo
Um material radioativo perde metade de sua massa a cada 50 segundos. Dada a massa inicial em gramas, escreva um programa que determine quanto tempo será necessário para que a massa fique menor que 0,5 grama.

Ao final, mostre:

a massa inicial
a massa final obtida
o tempo total decorrido
"""

mI = float(input("Digite a massa inicial em gramas: "))
mF = mI
count = 0

while mF >= 0.5:
    count += 50
    mF = mF / 2

print(f"massa inicial: {mI}")
print(f"massa final: {mF:.2f}")
print(f"tempo total: {count}s")