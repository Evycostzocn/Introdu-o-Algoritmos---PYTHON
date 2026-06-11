"""
Escreva uma função que receba uma tupla contendo notas de jurados em uma competição de ginástica. A função deve descartar a maior e a menor nota e retornar a
média das notas restantes. Lembre-se que tuplas são imutáveis. Na função principal,
faça um código que leia as notas e chame a função desenvolvida.
"""

def recebe_tupla(notas):
    maiorNota = notas[0]
    menorNota = notas[0]
    media = 0
    for i in range(len(notas)):
        if notas[i] > maiorNota:
            maiorNota = notas[i]
        elif notas[i] < menorNota:
            menorNota = notas[i]
        soma += notas[i]
    nova_soma = soma - maiorNota - menorNota
    media = nova_soma / (len(notas) - 2)
    return media
def main():
    qtdNotas = int(input("Digite quantas notas deseja contabilizar: "))
    listaNotas = []
    for i in range(qtdNotas):
        notas = float(input(f"Digite a nota {i + 1}: "))
        listaNotas.append(notas)
    listaNotasTupla = tuple(listaNotas) 
    media = recebe_tupla(listaNotasTupla)
    print(f"a média dos valores é {media:.2f}")

main()