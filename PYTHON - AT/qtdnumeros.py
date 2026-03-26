"""
Exercício 5 Quantidade de pares, ímpares, positivos e negativos
Escreva um programa que leia números inteiros até que seja digitado 0.

Ao final, o programa deve mostrar:

quantos números pares foram digitados
quantos números ímpares foram digitados
quantos números positivos foram digitados
quantos números negativos foram digitados
O zero apenas encerra a leitura.

Saída esperada:

Digite um número: 7
Digite um número: -4
Digite um número: 10
Digite um número: -3
Digite um número: 0
Pares: 2
Ímpares: 2
Positivos: 2
Negativos: 2"""

num = int(input("digite um número: "))
pares = 0
impares = 0
positivos = 0
negativos = 0

while num != 0:

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    else:
        negativos += 1

    num = int(input("digite um número: "))

print(f"Pares: {pares}")
print(f"ímpares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")