"""
Exercício 9 Controle de vendas de uma loja
Uma pequena loja deseja registrar as vendas realizadas durante um dia. Para isso, o operador do caixa informará o valor de cada venda, uma por vez. O processo deve continuar até que seja digitado o valor 0, indicando que não há mais vendas a registrar.

Escreva um programa que leia os valores das vendas e, ao final, mostre:

o valor total vendido no dia
a quantidade de vendas registradas
o valor médio das vendas
O valor 0 serve apenas para encerrar a entrada de dados e não deve ser considerado como venda.
"""

valorVenda = float(input("Digite o valor da venda: "))
valorTotal = 0
qtdVendas = 0
mediaVendas = 0

while valorVenda != 0:
    valorTotal += valorVenda
    qtdVendas += 1
    valorVenda = float(input("Digite o valor da venda: "))

mediaVendas = valorTotal / qtdVendas
print(f"Valor total: {valorTotal}")
print(f"Quantidade de vendas: {qtdVendas}")
print(f"Média das vendas: {mediaVendas}")