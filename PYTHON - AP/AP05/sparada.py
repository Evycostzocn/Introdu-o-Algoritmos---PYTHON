"""
Exercício 8 Soma até valor de parada
Escreva um programa que leia números inteiros indefinidamente, até que o usuário digite 0.

O valor 0 deve ser usado apenas como sinal de parada e não deve ser somado.

Ao final, o programa deve mostrar:

a soma de todos os números informados
a quantidade de números digitados, sem contar o zero
"""

numero = int(input("digite um número: "))

if numero == 0:
    print("Digitar 0 parará o programa!")
    exit()

soma = 0
countNumeros = 0

while numero != 0:
    soma += numero 
    countNumeros += 1
    numero = int (input("digite um número: "))
print(f"soma de todos os números: {soma}")
print(f"total de números digitados: {countNumeros}")
