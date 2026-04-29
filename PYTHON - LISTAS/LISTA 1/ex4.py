"""
Peça um valor inteiro positivo ao usuário e determine quantas cédulas de R$100,
R$50, R$20, R$10, R$5 e R$1 são necessárias para formar esse valor, utilizando
estruturas de repetição.
"""
valor = int(input("valor: "))

count_1 = 0
count_5 = 0
count_10 = 0
count_20 = 0
count_50 = 0
count_100 = 0


while valor >= 100:
    valor -= 100
    count_100 += 1
while valor >= 50:
    valor -= 50
    count_50 += 1
while valor >= 20:
    valor -= 20
    count_20 += 1
while valor >= 10:
    valor -= 10
    count_10 += 1
while valor >= 5:
    valor -= 5
    count_5 += 1
while valor >= 1:
    valor -= 1
    count_1 += 1

print(f"{count_100} nota(s) de 100")
print(f"{count_50} nota(s) de 50")
print(f"{count_20} nota(s) de 20")
print(f"{count_10} nota(s) de 10")
print(f"{count_5} nota(s) de 5")
print(f"{count_1} nota(s) de 1")

