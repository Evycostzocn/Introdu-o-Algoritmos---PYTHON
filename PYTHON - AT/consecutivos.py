"""
Exercício 9 Comparação entre números consecutivos
Escreva um programa que leia números inteiros até que seja digitado 0.

O programa deve comparar cada número digitado com o número anterior e contar:

quantas vezes foi digitado um número igual ao anterior
quantas vezes foi digitado um número maior que o anterior
quantas vezes foi digitado um número menor que o anterior
Considere que a primeira leitura serve apenas para iniciar a comparação.

Saída esperada:

Digite um número: 5
Digite um número: 5
Digite um número: 3
Digite um número: 7
Digite um número: 2
Digite um número: 0
Iguais ao anterior: 1
Maiores que o anterior: 1
Menores que o anterior: 2
"""

numero = int(input("digite um número: "))
countMaior = 0
countMenor = 0
countIgual = 0
maior = numero
menor = numero
igual = numero

while numero != 0:
    if numero > maior:
        maior = numero
        countMaior += 1
    elif numero < menor:
        menor = numero
        countMenor += 1
    else:
        igual = numero
        countIgual += 1
    numero = int(input("digite um número: "))
print(f"Iguais ao anterior: {countIgual}")
print(f"Maiores que o anterior: {countMaior}")
print(f"Menores que o anterior: {countMenor}")
    
