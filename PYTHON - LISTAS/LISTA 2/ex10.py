"""
Desenvolva um contador de frequência de palavras. O programa lê um parágrafo
de texto, divide em palavras, converte tudo para minúsculas e remove pontuações.
Utilize um dicionário (em que cada chave representa uma palavra encontrada no
texto, e cada valor representa a quantidade de vezes que essa palavra apareceu)
para contar quantas vezes cada palavra apareceu e, ao final, imprima as top 3
palavras mais frequentes."""

texto = input("Texto: ")

texto = texto.lower()

texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace("!", "")
texto = texto.replace("?", "")

palavras = texto.split()

dicionario = {}

for palavra in palavras:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1
print(dicionario)

maior_freq1 = 0
maior_freq2 = 0
maior_freq3 = 0

maior_palavra1 = ""
maior_palavra2 = ""
maior_palavra3 = ""

for palavra, frequencia in dicionario.items():

    if frequencia > maior_freq1:

        maior_freq3 = maior_freq2
        maior_palavra3 = maior_palavra2

        maior_freq2 = maior_freq1
        maior_palavra2 = maior_palavra1

        maior_freq1 = frequencia
        maior_palavra1 = palavra

    elif frequencia > maior_freq2:

        maior_freq3 = maior_freq2
        maior_palavra3 = maior_palavra2

        maior_freq2 = frequencia
        maior_palavra2 = palavra

    elif frequencia > maior_freq3:

        maior_freq3 = frequencia
        maior_palavra3 = palavra

print("TOP 3:")

print(maior_palavra1, "-", maior_freq1)
print(maior_palavra2, "-", maior_freq2)
print(maior_palavra3, "-", maior_freq3)
    