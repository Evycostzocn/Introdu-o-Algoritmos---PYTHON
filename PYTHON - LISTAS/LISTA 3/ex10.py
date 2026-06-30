# Crie uma função recursiva chamada
# maior_elemento(valores, indice)
# que receba uma lista de números inteiros e um índice e retorne o maior elemento
# existente entre a posição indicada e o final da lista.
# A chamada inicial deverá ser realizada da seguinte forma:
# maior_elemento(valores, 0)
# A função deve comparar o elemento da posição atual com o maior elemento encontrado nas posições seguintes.
# Não utilize:
# • estruturas de repetição dentro da função;
# • as funções max() ou sorted();
# • cópias ou fatiamentos da lista;
# • variáveis globais.
# No programa principal, leia uma lista com N números inteiros e exiba:
# • o maior elemento;
# • a primeira posição em que o maior elemento aparece;
# • a quantidade de vezes que ele aparece na lista.
# A contagem das ocorrências do maior elemento também deve ser realizada por uma
# função recursiva.

def maior_elemento(valores, indice):
    if indice == len(valores) - 1:
        return valores[indice]
    else:
        maior_resto = maior_elemento(valores, indice + 1)
        if valores[indice] > maior_resto:
            return valores[indice]
        else:
            return maior_resto

def contar_ocorrencias(valores, indice, valor):
    if indice == len(valores):
        return 0
    else:
        if valores[indice] == valor:
            return 1 + contar_ocorrencias(valores, indice + 1, valor)
        else:
            return contar_ocorrencias(valores, indice + 1, valor)
        
def primeira_posicao(valores, indice, valor):
    if indice == len(valores):
        return -1
    else:
        if valores[indice] == valor:
            return indice
        
        else:
            return primeira_posicao(valores, indice + 1, valor)

print(maior_elemento([1,2,3,4,5,4], 0))