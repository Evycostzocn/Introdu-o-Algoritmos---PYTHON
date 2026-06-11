"""
29. Um sensor de temperatura realiza medições e as guarda em uma lista. Sabendo
que o sensor às vezes falha e registra -999, crie uma função que receba a lista de
medições e substitua todos os -999 pela média aritmética dos dois valores válidos
adjacentes (o anterior e o próximo).
"""

def calcula_media(lista):
    anterior = 0
    proximo = 0
    for i in range(len(lista)):
        if lista[i] == -999:
            anterior = lista[i - 1]
            proximo = lista[i + 1]
            media = (anterior + proximo) / 2
            lista[i] = media
    return lista

qtd_medidos = int(input("Digite a quantidade de sensores que deseja medir: "))
lista = []
for i in range(qtd_medidos):
        medicoes = float(input(f"valor da medição {i + 1}: "))
        lista.append(medicoes)

novaLista = calcula_media(lista)

print(f"Nova lista: {novaLista}")