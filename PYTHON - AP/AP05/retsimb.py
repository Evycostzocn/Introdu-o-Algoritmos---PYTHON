"""
Exercício 12 Retângulo de símbolos
Leia dois valores inteiros: número de linhas e número de colunas. Depois, desenhe um retângulo usando o caractere *.

Exemplo para 3 linhas e 5 colunas:

*****
*****
*****
Este exercício deve ser resolvido com repetição aninhada usando while.
"""

"""
l = int(input("número de linhas: "))
c = int(input("número de colunas: "))

for i in range(1, l + 1):
    for j in range (1, c + 1):
        print("*", end="")
    print()
"""


l = int(input("número de linhas: "))
c = int(input("número de colunas: "))

i = l
j = c

while i > 0:
    linha = ""
    j = c
    while j > 0:
        linha += "*"
        j -= 1
    print(linha)
    i -= 1

