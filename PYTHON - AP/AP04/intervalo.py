"""
Exercício 1 Número dentro de um intervalo
Escreva um programa que leia um número inteiro informado pelo usuário.

O programa deve verificar se o número está entre 10 e 20.

Se o número estiver dentro desse intervalo, mostre:

Número dentro do intervalo
Caso contrário, mostre:

Número fora do intervalo
Desafio adicional

Versão A: utilizando dois if separados para verificar os limites do intervalo.
Versão B: utilizando um único if com operador lógico and."""

numero = int(input("Digite um numero: "))

if numero >= 10 and numero <= 20:
    print("Numero dentro do intervalo")
else:
    print("Numero fora do intervalo")