# 3. A secretaria de uma universidade armazena as notas dos alunos no arquivo notas.txt.
# Cada linha apresenta os dados de um aluno no seguinte formato:
# matricula;nome;nota1;nota2;nota3
# Desenvolva um programa que leia o arquivo e calcule a média de cada aluno. Considere a seguinte classificação:
# • média maior ou igual a 70: Aprovado;
# 2
# • média maior ou igual a 40 e menor que 70: Exame Especial;
# • média menor que 40: Reprovado.
# O programa deve gerar o arquivo resultado.txt, contendo, em cada linha:
# matricula;nome;media;situacao
# Além disso, o programa deve exibir:
# • a média geral da turma;
# • o nome e a média do aluno com maior desempenho;
# • a quantidade de alunos em cada situação;
# • a porcentagem de alunos aprovados;
# • a quantidade de registros inválidos.
# Um registro deve ser considerado inválido quando não possuir os cinco campos
# esperados, quando alguma nota não for numérica ou quando alguma nota estiver
# fora do intervalo de 0 a 100. Registros inválidos não devem participar dos cálculos.

with open("notas.txt", "r") as arq, open("resultados.txt", "w") as resultado:

    registros_invalidos = 0

    soma_media = 0
    qtd_alunos = 0

    aprovados = 0 # precisará da porcentagem de alunos aprovados
    exame = 0
    reprovados = 0

    maior_media = -1
    melhor_aluno = ""

    for linha in arq:
        partes = linha.strip().split(";")

        if len(partes) != 5:
            registros_invalidos += 1
            continue

        matricula = partes[0]
        nome = partes[1]
        nota1 = partes[2]
        nota2 = partes[3]
        nota3 = partes[4]

        try: 
            nota1 = float(nota1)
            nota2 = float(nota2)
            nota3 = float(nota3)

        except ValueError:
            registros_invalidos += 1
            continue

        if nota1 < 0 or nota1 > 100:
            registros_invalidos += 1
            continue
        
        if nota2 < 0 or nota2 > 100:
            registros_invalidos += 1
            continue

        if nota3 < 0 or nota3 > 100:
            registros_invalidos += 1
            continue

        media = (nota1 + nota2 + nota3) / 3

        if media >= 70:
            situacao = "Aprovado"
            aprovados += 1

        elif media >= 40:
            situacao = "Exame Especial"
            exame += 1
        
        else:
            situacao = "Reprovado"
            reprovados += 1

        soma_media += media
        qtd_alunos += 1

        if media > maior_media:
            maior_media = media
            melhor_aluno = nome
        
        resultado.write(f"{matricula};{nome};{media:.2f};{situacao}\n")
        
    if qtd_alunos > 0:
        porcentagem_aprovados = (aprovados / qtd_alunos) * 100
        media_geral = soma_media / qtd_alunos
    else:
        media_geral = 0
        porcentagem_aprovados = 0

print(f"Média geral da turma: {media_geral:.2f}")
print(f"Aluno com melhor desempenho: {melhor_aluno} || Nota: {maior_media:.2f}")
print(f"N° de aprovados: {aprovados} || N° de exames especiais: {exame} || N° de reprovados: {reprovados}")
print(f"Porcentagem de alunos aprovados: {porcentagem_aprovados:.2f}%")
print(f"Registros inválidos: {registros_invalidos}")