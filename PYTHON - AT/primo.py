"""

Exercício 5 Verificação de número primo
Escreva um programa que leia um número inteiro positivo n e verifique se ele é primo.

Um número primo é aquele que possui exatamente dois divisores: 1 e ele mesmo.

Saída esperada:

Digite um número: 13
O número é primo
Digite um número: 12
O número não é primo
"""

"""n = int(input("digite um numero: "))

while n != 0:
    if n % 3 == 0 and n % 1 == 0:
        print("numero primo")
    else:
        print("não é primo")
    break
"""

n = int(input("n: "))

i = 2

while n < 0:
    n = int(input("valor inválido"))

primo = True

while primo == True and i <= n / 2:
    if n % i == 0:
        primo = False
    i += 1

if primo == True:
    print("numero primo")
else:
    print("não é primo")