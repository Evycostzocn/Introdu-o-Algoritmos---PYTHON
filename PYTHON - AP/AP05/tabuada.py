"""
Exercício 4 Tabuada de um número
Escreva um programa que leia um número inteiro e mostre a sua tabuada de 1 a 10.

Exemplo: se o número informado for 7, o programa deve mostrar:

7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
"""

numero = int(input("digite um número: "))

if numero > 10:
    print("Número inválido, digite um número entre 1 e 10")
    exit()

tabuada = 0

for i in range(1, 10 + 1):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")
