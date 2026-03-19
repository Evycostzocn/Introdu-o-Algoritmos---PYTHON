nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
nota3 = float(input("Digite a nota da prova 3: "))

somaNotas = nota1 + nota2 + nota3
mediaNotas = (nota1 + nota2 + nota3) / 3
pontosParaTotal = 30 - somaNotas

print(f"Relatório de notas\n------------------\nSoma das notas: {somaNotas:.2f}\nMédia: {mediaNotas:.2f}\nPontos para média máxima: {pontosParaTotal}")