"""
Classificação de notas da turma
Escreva um programa que leia notas de alunos até que seja digitado um valor negativo.

Para cada nota lida, classifique-a da seguinte forma:

nota ≥ 8 e nota ≤ 10 → Ótimo
nota ≥ 7 e nota < 8 → Bom
nota ≥ 5 e nota < 7 → Regular
nota < 5 → Insatisfatório
Ao final, o programa deve mostrar quantas notas ficaram em cada faixa.

Saída esperada:

Digite uma nota: 8.5
Digite uma nota: 6.0
Digite uma nota: 4.0
Digite uma nota: 7.2
Digite uma nota: -1
Ótimo: 1
Bom: 1
Regular: 1
Insatisfatório: 1
"""

nota = float(input("digite uma nota: "))
otimo = 0
bom = 0
regular = 0
insatisfatorio = 0

while nota >= 0:

    if nota >= 8 and nota <= 10:
        otimo += 1
    elif nota >= 7 and nota < 8:
        bom += 1
    elif nota >= 5 and nota < 7:
        regular += 1
    else:
        insatisfatorio += 1
    nota = float(input("digite uma nota: "))

print(f"Ótimo: {otimo}")
print(f"Bom: {bom}")
print(f"Regular: {regular}")
print(f"Insatisfatório: {insatisfatorio}")