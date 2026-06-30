# 14. Uma aplicação precisa compactar pequenos textos substituindo sequências de caracteres iguais e consecutivos pelo caractere seguido da quantidade de repetições.
# Por exemplo:
# "aaabbccccdaa" -> "a3b2c4d1a2"
# "xxxx" -> "x4"
# "abc" -> "a1b1c1"
# Crie uma função recursiva chamada
# compactar_texto(texto, indice, caractere_atual, quantidade)
# que percorra o texto e retorne sua forma compactada.
# A função deve:
# • comparar o caractere da posição atual com o caractere que está sendo contabilizado;
# • aumentar a quantidade quando os caracteres forem iguais;
# • acrescentar o caractere e sua quantidade ao resultado quando uma nova sequência for iniciada;
# • incluir a última sequência de caracteres ao chegar ao final do texto;
# • tratar corretamente uma string vazia.
# Não utilize:
# • estruturas de repetição dentro da função recursiva;
# • bibliotecas externas de compactação;
# • variáveis globais.
# Crie também uma função recursiva chamada descompactar_texto(texto,
# indice) que realize a operação inversa.
# Por exemplo:
# "a3b2c4d1a2" -> "aaabbccccdaa"
# Considere que cada quantidade será um número inteiro entre 1 e 9.
# No programa principal:
# • leia textos até que seja informada a palavra "fim";
# • exiba o texto compactado;
# • descompacte o resultado;
# • verifique se o texto descompactado é igual ao texto original;
# • informe se a compactação reduziu, aumentou ou manteve o tamanho do texto

def compactar_texto(texto, indice, caractere_atual, quantidade):
    if texto == "":
        return ""

    if indice == len(texto):
        return caractere_atual + str(quantidade)

    if texto[indice] == caractere_atual:
        return compactar_texto(
            texto,
            indice + 1,
            caractere_atual,
            quantidade + 1
        )

    return (
        caractere_atual
        + str(quantidade)
        + compactar_texto(
            texto,
            indice + 1,
            texto[indice],
            1
        )
    )

def descompactar_texto(texto, indice):
    if indice == len(texto):
        return ""

    caractere = texto[indice]
    quantidade = int(texto[indice + 1])

    return (
        caractere * quantidade
        + descompactar_texto(texto, indice + 2)
    )

while True:
    texto = input("Texto: ")

    if texto == "fim":
        break

    compactado = compactar_texto(texto, 1, texto[0], 1)

    print("Compactado:", compactado)

    descompactado = descompactar_texto(compactado, 0)

    print("Descompactado:", descompactado)

    if texto == descompactado:
        print("Texto recuperado corretamente!")

    if len(compactado) < len(texto):
        print("A compactação reduziu o tamanho.")

    elif len(compactado) > len(texto):
        print("A compactação aumentou o tamanho.")

    else:
        print("A compactação manteve o tamanho.")