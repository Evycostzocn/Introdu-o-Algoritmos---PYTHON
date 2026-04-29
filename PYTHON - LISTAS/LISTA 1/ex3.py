"""
Peça ao usuário um número binário (por exemplo: 1101), e converta-o para decimal
utilizando um while
"""

"""
binario = int(input("digite o numero binario: "))
decimal = 0
potencia = 0

while binario > 0:
    digito = binario % 10
    decimal += digito * pow(2,potencia)
    potencia += 1
    binario = binario // 10
print(decimal)
"""

binario = input("binario: ")
potencia = 0
resultado = 0

while len(binario) > 0:
    digito = int(binario[-1]) # pega o ultimo elemento
    resultado += digito *(2 ** potencia)
    potencia += 1
    binario = binario[:-1] # pega tudo, menos o ultimo caracter
print(resultado)
