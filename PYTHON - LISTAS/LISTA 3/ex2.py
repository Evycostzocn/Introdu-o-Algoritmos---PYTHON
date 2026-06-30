# 2. Dois arquivos, chamados nomes1.txt e nomes2.txt, armazenam nomes de pessoas em ordem alfabética, 
# com um nome em cada linha. Os arquivos podem possuir
# quantidades diferentes de nomes.
# Desenvolva um programa que crie o arquivo nomes_mesclados.txt, contendo
# todos os nomes dos dois arquivos também em ordem alfabética.
# A mesclagem deve ser realizada comparando a linha atual de cada arquivo, de
# maneira semelhante à etapa de intercalação de duas sequências ordenadas.
# Para esta questão:
# • não utilize a função sort() ou o método sort();
# • não reúna inicialmente todos os nomes em uma única lista para depois ordenálos;
# • nomes repetidos nos dois arquivos devem aparecer apenas uma vez no arquivo
# resultante;
# • ao final de um dos arquivos, todas as linhas ainda não processadas do outro
# arquivo devem ser copiadas.
# Além de gerar o novo arquivo, o programa deve informar:
# • quantos nomes foram lidos do primeiro arquivo;
# • quantos nomes foram lidos do segundo arquivo;
# • quantos nomes distintos foram gravados no arquivo resultante.

with open("nomes1.txt", "r") as arq1:
    nomes1 = []
    for linha in arq1:
        nomes1.append(linha.strip())

with open("nomes2.txt", "r") as arq2:
    nomes2 = []
    for linha in arq2:
        nomes2.append(linha.strip())
i = 0
j = 0
 
resultado = []

while i < len(nomes1) and j < len(nomes2):
    if nomes1[i] < nomes2[j]:
        resultado.append(nomes1[i])
        i += 1
    elif nomes2[j] < nomes1[i]:
        resultado.append(nomes2[j])
        j += 1
    else:
        resultado.append(nomes1[i])
        i += 1
        j += 1
    
while i < len(nomes1):
    resultado.append(nomes1[i])
    i += 1
while j < len(nomes2):
    resultado.append(nomes2[j])
    j += 1

with open("nomes_mesclados.txt", "w") as arq:
    for nome in resultado:
        arq.write(nome + "\n")

print(f"Quantidade de nomes lidos no 1° arquivo: {len(nomes1)}")
print(f"Quantidade de nomes lidos no 2° arquivo: {len(nomes2)}")
print(f"Quantidade de nomes gravados no novo arquivo: {len(resultado)}")