"""
26. Desenvolva um programa que leia os preços de N produtos em um carrinho de
compras. Crie uma função que aplique um desconto progressivo na lista: 5% para
itens acima de R$ 100, e 10% para itens acima de R$ 500. A função deve retornar
a lista de preços atualizada e o valor total economizado.
"""

def aplica_desconto(lista):
    novaLista = []
    valorEconomizado = 0
    soma = 0
    for i in lista:
        valorSemDesconto = lista[i]
        if lista[i] > 100:
            valor = lista[i] - (lista[i] * (5 / 100))
            novaLista.append(valor)
        if lista[i] > 500:
            valor = lista[i] - (lista[i] * (10 / 100))
            novaLista.append(valor)
        soma += valor
    

def main():
    lista = []
    while True:
        n = float(input("n: "))
        if n == 0:
            break
        lista.append(n)
    novaLista, valorEconomizado = aplica_desconto(lista)