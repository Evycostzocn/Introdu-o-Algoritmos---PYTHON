"""
Exercício 5 Média de 5 notas
Escreva um programa que leia 5 notas informadas pelo usuário e, ao final, calcule e mostre a média aritmética dessas notas.

Este exercício exige o uso de repetição com contador e acumulador.
"""

media = 0
soma = 0

for i in range(1, 5 + 1):
    nota = float (input("digite uma nota: "))
    soma += nota
    media = soma / i
print(media)