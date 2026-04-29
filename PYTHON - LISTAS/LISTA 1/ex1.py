"""
Peça um número inteiro positivo ao usuário e determine se ele é primo utilizando
while.
"""

n = int(input("n: "))
count_div = 0
i = 1

while i <= n:

    if n % i == 0:
        count_div += 1
    i += 1

if count_div == 2:
    print("é primo")

else:
    print("não é primo") 