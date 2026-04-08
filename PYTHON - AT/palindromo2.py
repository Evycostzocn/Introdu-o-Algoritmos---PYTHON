"""
Dada uma string, escreva um programa que verifique, para cada prefixo dessa
string, se ele é um palíndromo. Um prefixo é qualquer parte inicial da string,
formada pelos primeiros caracteres, sem pular posições. Uma string é considerada
palíndromo quando pode ser lida da mesma forma da esquerda para a direita e da
direita para a esquerda.
Seu programa deve ler um texto digitado pelo usuário e exibir quais prefixos são
palíndromos, por exemplo:
⏳ Agora, é sua vez!
25
>>> Digite o texto: AABAA
A
AA
AABAA
"""

palavra = input("Digite uma palavra: ")
prefixo = ""

for i in range(len(palavra)):
    eh_palindromo = True
    prefixo += palavra[i]
    for j in range(i + 1):
        if palavra[j] != palavra[i - j]:
            eh_palindromo = False
    if eh_palindromo:
        print(prefixo)