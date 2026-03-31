"""
Exercício 10 Monitoramento de temperaturas de uma máquina
Uma máquina industrial possui um sensor que registra sua temperatura ao longo da operação. Para analisar o funcionamento do equipamento, um técnico deseja criar um programa que permita inserir várias temperaturas registradas durante o dia.

O programa deve ler temperaturas em graus Celsius, uma por vez, até que o usuário digite o valor -1, que indica o fim da coleta.

Ao final, o programa deve informar:

quantas temperaturas foram registradas
a maior temperatura
a menor temperatura
a média das temperaturas
quantas temperaturas estavam acima de 80 graus
O valor -1 é apenas o marcador de encerramento e não deve ser considerado nos cálculos.
"""

temperatura = float(input("Digite uma temperatura em celsius: "))

countTemp = 0
maiorTemp = temperatura
menorTemp = temperatura
temperatura_maior_80 = 0
somaTemp = 0

if temperatura == -1:
    print("Digitar -1 parará o programa")
    exit()

while temperatura != -1:
    somaTemp += temperatura
    if temperatura > 80:
        temperatura_maior_80 += 1
    
    if temperatura > maiorTemp:
        maiorTemp = temperatura
    elif temperatura < menorTemp:
        menorTemp = temperatura
    countTemp += 1

    temperatura = float(input("Digite uma temperatura em celsius: "))

mediaTemp = somaTemp / countTemp

print(f"temperaturas registradas: {countTemp}")
print(f"maior temperatura: {maiorTemp}")
print(f"menor temperatura: {menorTemp}")
print(f"média das temperaturas: {mediaTemp}")
print(f"temperaturas acima de 80 graus: {temperatura_maior_80}")
