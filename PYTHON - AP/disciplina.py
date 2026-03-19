"""
Exercício 5 Sistema de aprovação em disciplina
Uma disciplina utiliza dois critérios para aprovação:

média final
frequência
O programa deve ler:

média do aluno
percentual de frequência
As regras são:

Se a frequência for menor que 75%, o aluno está reprovado por falta.
Caso contrário, analisar a média:
média ≥ 60 → aprovado
média entre 40 e 59 → recuperação
média abaixo de 40 → reprovado por nota
O programa deve mostrar o resultado final do aluno.

Desafio adicional

Versão A: utilizando condicionais aninhadas.
Versão B: tentando reduzir o número de níveis de aninhamento usando operadores lógicos (and)."""


media = float(input("Média do aluno: "))
frequencia = int(input("Frequência do aluno: "))

if media > 100:
    media = float(input("Digite a nota real: "))
if frequencia < 75:
    print("Reprovado por falta.")
elif media >= 60 and media <= 100:
    print("Aprovado")
elif  media >= 40 and media <= 60:
    print("Recuperação")
else:
    print("Reprovado por nota")
