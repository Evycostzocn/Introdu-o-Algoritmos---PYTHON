# Crie um sistema de reservas de poltronas de um teatro representado por uma matriz
# 10 × 10, inicializada com 0 (livre). O usuário informa linha e coluna para reservar.
# Crie funções para: reservar(M, l, c), que marca com 1 o local, se esse local
# estiver livre; e verificar_lotacao(M), que retorna a porcentagem de ocupação
# total do teatro.

def reservar(M, l, c): 
    if M[l][c] == 0:
        M[l][c] = 1
    else:
        print("POLTRONA OCUPADA")
    
def verificar_lotacao(M):
    count_ocupado = 0
    for i in range(10):
        for j in range(10):
            if M[i][j] == 1:
                count_ocupado += 1
    total_poltronas = len(M) * len(M[0])
    porcentagem = (count_ocupado / total_poltronas) * 100
    return porcentagem

matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        linha.append(0)
    matriz.append(linha)

l = int(input("Linha: "))
c = int(input("Coluna: "))

reservar(matriz, l, c)
ocupacao = verificar_lotacao(matriz)
print(ocupacao)
