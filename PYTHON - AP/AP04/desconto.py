"""Exercício 3 Elegibilidade para desconto
Uma loja oferece desconto especial para clientes que atendem a uma das seguintes condições:

idade maior ou igual a 60 anos
valor da compra maior que 200 reais
Escreva um programa que leia:

idade do cliente
valor da compra
Se o cliente tiver direito ao desconto, mostre:

Cliente elegível para desconto
Caso contrário, mostre:

Cliente sem desconto
Desafio adicional

Versão A: utilizando dois if separados.
Versão B: utilizando um único if com operador lógico or."""


idade = int(input("Idade: "))
valor = float(input("Valor da compra: "))

if idade >= 60 or valor > 200:
    print("Cliente elegível para compra")
else:
    print("Cliente não elegível")