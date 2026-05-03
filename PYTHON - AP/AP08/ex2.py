
"""
Exercício 6 Verificação de nota válida
Crie uma função chamada nota_valida(nota) que receba uma nota e retorne:

True, se a nota estiver entre 0 e 100, inclusive;
False, caso contrário.
No programa principal:

leia uma nota;
exiba o resultado retornado.
"""

"""
Exercício 7 Classificação de desempenho
Crie uma função chamada classificar_desempenho(nota) que receba uma nota de 0 a 100 e retorne:

"Excelente" para notas de 90 a 100;
"Bom" para notas de 70 a 89;
"Regular" para notas de 60 a 69;
"Insuficiente" para notas abaixo de 60.
No programa principal:

leia uma nota;
exiba a classificação retornada.
"""

"""
Exercício 8 Cálculo da situação final
Crie uma função chamada calcular_situacao(nota) que receba uma nota de 0 a 100 e retorne:

"Aprovado", se a nota for maior ou igual a 70;
"Recuperação", se a nota estiver entre 50 e 69;
"Reprovado", caso contrário.
No programa principal:

leia uma nota;
exiba a situação retornada.
"""

"""
Crie uma função chamada gerar_resumo_correcao(nota) que receba uma nota e retorne dois valores:

a classificação de desempenho;
a situação final do aluno.
Importante: para resolver este exercício, utilize as funções criadas nos exercícios 7 e 8 dentro da nova função.

No programa principal:

leia uma nota;
chame a função;
exiba os dois valores retornados.
"""

def nota_valida(nota):
    if nota >= 0 and nota <= 100:
        return True
    else:
        return False

def classificar_desempenho(nota):
    if nota >= 90 and nota <= 100:
        print("Execelente") 
    elif nota >= 70 and nota <= 89:
        print("Bom") 
    elif nota >= 60 and nota <= 69:
        print("Regular") 
    else:
        print("Insuficiente")

def calcular_situacao(nota):
    if nota >= 70:
        print("Aprovado")
    elif nota >= 50 and nota <= 69:
        print("Recuperação")
    else:
        print("Reprovado")

def gerar_resumo_correcao(nota):
    classificar_desempenho(nota)
    calcular_situacao(nota)
    

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))

    gerar_resumo_correcao(nota)

