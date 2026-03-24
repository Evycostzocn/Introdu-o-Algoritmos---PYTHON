"""
Soma dos valores digitados
Escreva um programa que leia números inteiros digitados pelo usuário até que seja digitado 0.

Ao final, o programa deve mostrar a soma de todos os valores digitados, sem considerar o zero.

Saída esperada:

Digite um número: 4
Digite um número: 7
Digite um número: -2
Digite um número: 0
Soma dos valores: 9"""

num = int(input("digite um número: "))
soma = 0

while num != 0:
    soma += num
    num = int(input("digite um número: "))
print(soma)