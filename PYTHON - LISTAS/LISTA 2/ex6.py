"""
Uma plataforma acadêmica possui a lista de alunos matriculados em "Algoritmos" e
a lista de alunos matriculados em "Cálculo". O programa deve ler N matrículas para
cada disciplina. Utilizando a estrutura de Conjuntos (set), determine e imprima:
os alunos matriculados em ambas as disciplinas, e os alunos matriculados em apenas
uma das disciplinas.
"""

calculo = set()
algoritmos = set()

while True:

    aluno = input("Nome do aluno(a): ")

    faz_calculo = input("Aluno matriculado em Cálculo (s/n): ")
    faz_algoritmos = input("Aluno matriculado em Algortmos (s/n): ")

    if faz_calculo == "s":
        calculo.add(aluno)
    if faz_algoritmos == "s":
        algoritmos.add(aluno)

    continuar = input("Deseja continuar o programa (s/n): ")
    if continuar != "s":
        break

print(f"Ambas as disciplinas: {calculo & algoritmos}")
print(f"Apenas uma disciplina: {calculo ^ algoritmos}")