"""
Crie um programa que leia 20 números inteiros e os armazene em uma lista. Crie
uma função eliminar_duplicatas(lista) que retorne uma nova lista contendo os mesmos elementos, mas mantendo apenas a primeira ocorrência de cada
número (preservando a ordem original). Observação: Não utilize conjuntos (sets)
para resolver a questão.
"""

def eliminar_duplicatas(lista):
    nova_lista = []
    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)
    return nova_lista

lista = []

for i in range(20):
    numero = int(input("Digite um número: "))
    lista.append(numero)

novaLista = eliminar_duplicatas(lista)

print(novaLista)