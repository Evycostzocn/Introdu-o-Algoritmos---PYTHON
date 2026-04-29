"""
Peça ao usuário que informe uma sequência de números inteiros. A leitura deve
ser encerrada quando o valor 0 for digitado (o valor 0 não deve ser considerado na
sequência).
Um trecho da sequência é considerado crescente consecutivo quando cada número é
estritamente maior que o anterior. Desenvolva um programa que determine o maior
tamanho de um trecho crescente consecutivo presente na sequência informada.
Exemplo:
Entrada: 3, 5, 7, 2, 4, 6, 8, 1, 0
Saída: 4
(Referente ao trecho: 2, 4, 6, 8)
"""
numero = int(input("digite um numero (0 para o programa): "))

atual = 1
maior = 1
anterior = numero

while True:
    numero = int(input("digite um numero (0 para o programa): "))
    if numero == 0:
        break

    if numero > anterior:
        atual += 1
    else:
        atual = 1
    if atual > maior:
        maior = atual
    anterior = numero
print(maior)
