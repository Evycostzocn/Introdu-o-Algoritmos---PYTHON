"""
O sistema de rastreamento de entregas armazena o percurso de um caminhão como
uma lista de tuplas (latitude, longitude). Escreva uma função que receba
essa lista e calcule a distância total percorrida. Para simplificar, considere a distância entre os pontos (x1, y1) e (x2, y2) como q
raiz de (x2 − x1)^2 + (y2 − y1)^2
"""

import math
distancia_total = 0
rotas = []
qtd_pontos = int(input("Digite a quantidade de pontos a serem contados: "))
for i in range(qtd_pontos):
    x = int(input("x: "))
    y = int(input("y: "))
    ponto = (x, y)
    rotas.append(ponto)
for i in range(len(rotas) - 1):
    x1, y1 = rotas[i]
    x2, y2 = rotas[i + 1]
    distancia = math.sqrt(
        ((x2 - x1) ** 2) 
        + ((y2 - y1) ** 2)
     )  
    distancia_total += distancia
    print(f"Distância: {distancia:.2f}")
print(f"Distância total: {distancia_total:.2f}")