"""
Projete um algoritmo que leia números inteiros positivos, rejeite valores inválidos,
pare quando o usuário digitar zero e informe quantidade, média, maior e menor
valor. Descreva invariantes do algoritmo, o fluxo lógico da solução, identifique casos
críticos e implemente.
"""

n = int(input("n: "))
count = 0
soma = 0


for i in range(1, n + 1):

    if n == 0 or n < 0:
        print("valor inválido")
        exit()

    maior = n
    menor = n   

    n = int(input("n: "))

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    soma += n
    count += 1

media = soma / count
print(f"{media:.2f}")
print(f"maior numero: {maior}")
print(f"menor numero: {menor}")
print(f"quantidade de numero: {count}")