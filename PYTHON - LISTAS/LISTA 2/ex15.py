# Peça ao usuário que informe uma sequência de números inteiros, parando ao digitar
# 0. Armazene os números em uma lista. Desenvolva uma função que receba essa
# lista e determine o tamanho do maior trecho crescente consecutivo presente.


n = int(input("digite um numero: "))

listaNum = []
atual = 1
maior = 1

while n != 0:
    listaNum.append(n)
    n = int(input("digite um numero: "))

for i in range(1, len(listaNum)):
    if listaNum[i] > listaNum[i - 1]:
        atual += 1
    else:
        atual = 1

    if atual > maior:
        maior = atual

print(f"maior trecho: {maior}")