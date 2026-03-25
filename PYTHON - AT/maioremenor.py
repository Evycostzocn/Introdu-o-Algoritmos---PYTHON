"""
Exercício 7 Maior e menor número digitado
Escreva um programa que leia números inteiros até que seja digitado 0.

Ao final, o programa deve mostrar:

o maior número digitado
o menor número digitado
Atenção: se nenhum valor for digitado antes do zero, o programa deve mostrar a mensagem Nenhum valor foi informado.

Saída esperada:

Digite um número: 4
Digite um número: 9
Digite um número: -2
Digite um número: 15
Digite um número: 0
Maior número: 15
Menor número: -2
"""

num = int(input("digite um numero: "))
menor = 0 
menorNum = 0
maior = 0
maiorNum = 0

while num != 0:
    if num < menor:
        menor = menorNum
    else:
        maior = maiorNum
    num = int(input("digite um numero: "))
print(menorNum)
print(maiorNum)