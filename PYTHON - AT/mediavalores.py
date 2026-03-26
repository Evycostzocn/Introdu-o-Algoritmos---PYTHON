"""
Exercício 6 Média dos valores digitados
Escreva um programa que leia números reais até que seja digitado 0.

Ao final, o programa deve calcular e mostrar a média dos valores digitados, sem considerar o zero.

Atenção: se nenhum valor for digitado antes do zero, o programa deve mostrar a mensagem Nenhum valor válido foi informado.

Saída esperada:

Digite um número: 6
Digite um número: 8
Digite um número: 4
Digite um número: 0
Média: 6.0
"""
num = int (input ("digite um número: "))
count = 0
soma = 0
media = 0

while num != 0:
    soma += num
    num = int(input("digite um número: "))
    count += 1
if count == 0:
    print("Nenhum valor válido foi informado")
else:
    media = soma / count
    print(media)