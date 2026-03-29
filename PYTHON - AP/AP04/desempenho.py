"""
Exercício 4 Classificação de desempenho
Um sistema de avaliação classifica o desempenho de um aluno com base na nota final (0 a 100).

As classificações são as seguintes:

90 a 100 → Excelente
70 a 89 → Bom
50 a 69 → Regular
abaixo de 50 → Insuficiente
O programa deve ler a nota do aluno e mostrar apenas uma classificação."""

notaAluno = float(input("Nota: "))

if notaAluno >= 90 and notaAluno <= 100:
    print("Excelente")
elif notaAluno >= 70 and notaAluno <= 89:
    print("Bom")
elif notaAluno >= 50 and notaAluno <= 69:
    print("Regular")
else:
    print("Insuficiente")
