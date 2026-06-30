# 11. Crie uma função recursiva chamada
# contar_ocorrencias(valores, procurado, indice)
# que receba uma lista de números inteiros, um valor procurado e a posição a partir
# da qual a busca deve ser realizada.
# A função deve retornar quantas vezes o valor procurado aparece na lista.
# Por exemplo:
# valores = [4, 7, 4, 2, 4, 9]
# contar_ocorrencias(valores, 4, 0) -> 3
# cselfontar_ocorrencias(valores, 8, 0) -> 0
# Além da função de contagem, crie uma segunda função recursiva chamada
# primeira_posicao(valores, procurado, indice)
# que retorne o índice da primeira ocorrência do valor procurado ou -1, caso ele não
# esteja presente.
# No programa principal, leia a lista e um valor a ser pesquisado. Exiba a quantidade
# de ocorrências e a primeira posição encontrada.
# Não utilize os métodos count() e index().

def contar_ocorrencias(valores, procurado, indice):
    if indice == len(valores):
        return 0
    else:
        if valores[indice] == procurado:
           return 1 + contar_ocorrencias(valores, procurado, indice + 1)
        else:
            return contar_ocorrencias(valores, procurado, indice + 1)
def primeira_posicao(valores, procurado, indice):
    if indice == len(valores):
        return -1
    else:
        if valores[indice] == procurado:
            return indice
        else:
            return primeira_posicao(valores, procurado, indice + 1)
        
lista = []

n = int(input("tamanho da lista: "))

for i in range(n):
    valores = int(input("digite um valor: "))
    lista.append(valores)

valor_pesquisado = int(input("valor a ser pesquisado: "))

ocorrencias = contar_ocorrencias(lista, valor_pesquisado, 0)

primeiraPosicao = primeira_posicao(lista, valor_pesquisado, 0)

print(f"Ocorrências: {ocorrencias}")
print(f"Primeira posição: {primeiraPosicao}")

