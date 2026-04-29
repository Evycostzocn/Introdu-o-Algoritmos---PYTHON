"""
Peça ao usuário que informe uma sequência de números inteiros. A leitura deve
ser encerrada quando o valor 0 for digitado (o valor 0 não deve ser considerado na
sequência).
Um padrão é identificado quando ocorre uma sequência de pelo menos três números
consecutivos iguais.
Desenvolva um programa que verifique se existe esse padrão na sequência informada.
Exemplos:
Entrada: 1, 2, 2, 2, 3, 0
Saída: Existe padrão
Entrada: 1, 2, 2, 3, 0
Saída: Não existe padrão
"""
numero = int(input("digite um numero (0 para o programa): "))

igual = 1
anterior = numero
encontrou = False

while True:
    numero = int(input("digite um numero (0 para o programa): "))

    if numero == 0:
        break

    if numero == anterior:
        igual += 1
    else:
         igual = 1
         
    if igual >= 3:
            encontrou = True
    anterior = numero

if encontrou:
    print("Existe padrão")
else:
    print("Não existe padrão")