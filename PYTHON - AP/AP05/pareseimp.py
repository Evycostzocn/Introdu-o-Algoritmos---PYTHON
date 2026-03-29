"""
Exercício 6 Contador de números pares e ímpares
Escreva um programa que leia 10 números inteiros.

Ao final, o programa deve mostrar:

quantos números eram pares
quantos números eram ímpares
"""

countPares = 0
countImpares = 0

for i in range (1, 10 + 1):
    numero = int(input("digite um número: "))
    if numero % 2 == 0:
        countPares += 1
    else:
        countImpares += 1

print(f"quantidade de números pares: {countPares}")
print(f"quantidade de números impares: {countImpares}")