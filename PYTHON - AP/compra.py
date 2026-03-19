"""
Exercício 4 Compra Online
Calcule o valor final de um produto comprado pela internet.

Leia:

preço do produto
percentual de imposto (valor de 0 a 100)
valor do frete

Calcule e apresente:

Valor de imposto a ser cobrado
Valor total (preço somado ao imposto e frete)
Saída esperada:

Resumo da compra
----------------
Valor do imposto: ...
Valor total: ..."""

preco = float(input("Digite o preço do produto: "))
imposto = float(input("Digite o percentual do imposto: "))
frete = float(input("Digite o valor do frete: "))

valorImposto = preco * (imposto / 100)
valorTotal = preco + valorImposto + frete

print(f"Resumo da compra\n----------------\nValor do imposto: {imposto}\nValor total: {valorTotal}")
