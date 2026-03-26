"""
Exercício 7 Maior e menor valor informados
Escreva um programa que leia 8 números inteiros e determine:

o maior valor informado
o menor valor informado
Ao final, mostre os dois resultados.
"""

numero = int(input("digite um número: "))
menor = numero
maior = numero
for i in range(1, 8):
    numero = int(input("digite um número: "))

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print(f"maior valor informado: {maior}")
print(f"menor valor informado: {menor}")