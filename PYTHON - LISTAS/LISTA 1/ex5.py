"""
Faça um programa de um jogo de adivinhação. O programa deve gerar um número
aleatório entre 1 e 10. O usuário deve informar palpites, e o programa deve indicar
se o número correto é maior ou menor. O jogo continua até que o usuário acerte.
"""

numero = int(input("digite um número: "))
secreto = (numero % 10) + 1
palpite = 0

while palpite != secreto:
    palpite = int(input("digite o valor do palpite: "))

    if palpite > secreto:
        print("numero correto é menor")
    elif palpite < secreto:
        print("numero correto é maior")
    else:
        print("acertou!")
        break