"""
Exercício 1 Guardando e exibindo números
Crie um programa em Python que leia 5 números inteiros digitados pelo usuário e armazene todos eles em uma lista.

O programa deve exibir:

a lista completa;
cada elemento da lista, um por linha.
Exemplo de entrada
10
5
8
2
7
Saída esperada
Lista completa: [10, 5, 8, 2, 7]
10
5
8
2
7
Observação: criar uma lista, adicionar elementos com append e percorrer uma lista, usando as duas formas possíveis de percurso com for (por índice e por valor).
"""

lista = []

for i in range(5):
    numero = int(input("numero: "))
    lista.append(numero)

for numero in lista:
    print(numero)