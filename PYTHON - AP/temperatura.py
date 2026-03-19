"""
Exercício 2 Classificação de temperatura
Escreva um programa que leia a temperatura atual em graus Celsius.

O programa deve verificar as seguintes situações:

se a temperatura é menor que 10
se a temperatura está entre 10 e 25
se a temperatura é maior que 25
Para cada situação, o programa deve mostrar:

Temperatura baixa
Temperatura agradável
Temperatura alta
Desafio adicional

Versão A: utilizando vários if independentes.
Versão B: utilizando operadores lógicos (and) para verificar intervalos, e exclusão mútua."""

temperatura = float(input("Digite a temperatura em celsius: "))

if temperatura < 10:
    print("temperatura baixa")
elif temperatura <= 25:
    print("Temperatura agradável")
else:
    print("Temperatura alta")
