"""
Crie um jogo em que o usuário escolhe par ou ímpar, informa um número e joga
contra o computador (que gera um número aleatório). O programa deve mostrar o
resultado da soma, identificar se é par ou ímpar e informar o vencedor. O jogo deve
se repetir até o usuário desejar sair.
"""

import random

while True:
    escolha = int(input("digite 1 para PAR e 2 para ÍMPAR: "))
    numero = int(input("digite um número: "))

    num_computador = random.randint(1, 100)

    print(f"computador jogou: {num_computador}")

    soma = numero + num_computador
    print(f"Resultado da soma: {soma}")

    if soma % 2 == 0:
        print("É PAR")
        if escolha == 1:
            print("USER VENCEU")
        else:
            print("BOT VENCEU")
    else:
        print("É ÍMPAR!")
        if escolha == 2:
            print("USER VENCEU")
        else:
            print("BOT VENCEU")
    continuar = input("Deseja continuar o jogo? (s/n): ")
    if continuar != "s":
        break


