"""
Exercício 11 Tabuada completa de 1 a 9
Escreva um programa que mostre todas as tabuadas de multiplicação de 1 a 9.

Exemplo de estrutura esperada:
Tabuada do 1
1 x 1 = 1
...
1 x 10 = 10

Tabuada do 2
2 x 1 = 2
...
"""

numero = 1

for i in range (1, 9 + 1):
    print(f"Tabuada do {i}")

    for j in range (1, 10 + 1):
        tabuada = numero * j
        print(f"{numero} x {j} = {tabuada}")
    numero += 1
    
"""
for i in range(1, 9 + 1)
    print(f"Tabuada do {i}")
    
    for j in range (1, 10 + 1)
        print(f"{i} x {j} = {i * j})
"""
