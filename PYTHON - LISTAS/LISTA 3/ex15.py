# 15. Um robô foi colocado em um labirinto representado por uma matriz. Cada posição
# da matriz contém um dos seguintes valores:
# • 0: posição livre;
# • 1: parede;
# • 2: posição inicial do robô;
# • 3: posição de saída.
# O robô pode se movimentar uma posição por vez para cima, para baixo, para a
# esquerda ou para a direita.
# Crie uma função recursiva chamada
# encontrar_saida(labirinto, linha, coluna)
# que utilize a técnica de tentativa e retrocesso (backtracking) para encontrar um
# caminho entre a posição inicial e a saída.
# A função deve:
# • retornar False ao acessar uma posição fora dos limites da matriz;
# • retornar False ao encontrar uma parede;
# • retornar False ao encontrar uma posição já visitada;
# • retornar True ao alcançar a saída;
# • marcar temporariamente as posições visitadas;
# • tentar os quatro movimentos possíveis;
# • desfazer a marcação quando uma posição não fizer parte do caminho que leva
# à saída.
# Quando um caminho for encontrado, as posições que fazem parte dele devem ser
# marcadas com o valor 4.
# No programa principal:
# • leia as dimensões e os valores do labirinto;
# • localize a posição inicial do robô;
# • chame a função recursiva;
# • informe se existe um caminho até a saída;
# • exiba a matriz com o caminho encontrado;
# • informe a quantidade de posições percorridas no caminho.
# Não utilize estruturas de repetição dentro da função recursiva. As estruturas de
# repetição podem ser utilizadas no programa principal para ler e exibir a matriz.

def encontrar_saida(labirinto, linha, coluna):
    if linha < 0 or linha >= len(labirinto):
        return False
    
    if coluna < 0 or coluna >= len(labirinto[0]):
        return False
    
    if labirinto[linha][coluna] == 1:
        return False
    
    if labirinto[linha][coluna] == 99:
        return False

    if labirinto[linha][coluna] == 3:
        return True
    
    labirinto[linha][coluna] = 99
    
    if encontrar_saida(labirinto, linha - 1, coluna):
        labirinto[linha][coluna] = 4
        return True
    
    if encontrar_saida(labirinto, linha + 1, coluna):
        labirinto[linha][coluna] = 4
        return True
    
    if encontrar_saida(labirinto, linha, coluna + 1):
        labirinto[linha][coluna] = 4
        return True
    
    if encontrar_saida(labirinto, linha, coluna - 1):
        labirinto[linha][coluna] = 4
        return True
    
    labirinto[linha][coluna] = 0

    return False

matriz = []

l = int(input("numero de linhas: "))
c = int(input("numero de colunas: "))

for i in range(l):
    linha = []
    for j in range(c):
        valor = int(input("valor: "))
        linha.append(valor)
    matriz.append(linha)

linha_inicial = 0
coluna_inicial = 0

for i in range(l):
    for j in range(c):
        if matriz[i][j] == 2:
            linha_inicial = i
            coluna_inicial = j

achou = encontrar_saida(matriz, linha_inicial, coluna_inicial)

if achou:
    print("Existe um caminho")
else:
    print("Não existe caminho")

print("\nLabirinto:")
for linha in matriz:
    print(linha)

quantidade = 0

for i in range(l):
    for j in range(c):
        if matriz[i][j] == 4:
            quantidade += 1

print(f"Quantidade de posições do caminho: {quantidade}")
