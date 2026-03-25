"""
Soma apenas dos números pares
Escreva um programa que leia números inteiros até que seja digitado 0.

Durante a leitura, o programa deve somar apenas os valores pares.

Ao final, imprima a soma calculada.

Saída esperada:

Digite um número: 5
Digite um número: 8
Digite um número: 11
Digite um número: 2
Digite um número: 0
Soma dos pares: 10"""

numero = int(input("digite um número: "))
soma = 0

while numero != 0:
    if numero % 2 == 0:
        soma += numero
    numero = int(input("digite um número: "))
print(soma)