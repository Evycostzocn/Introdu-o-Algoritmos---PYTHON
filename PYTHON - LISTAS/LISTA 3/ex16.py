# 16. Crie uma função recursiva chamada converter_binario(n) que receba um
# número inteiro não negativo e retorne uma string contendo sua representação em
# base binária.
# Por exemplo:
# converter_binario(13) -> "1101"
# converter_binario(8) -> "1000"
# converter_binario(0) -> "0"
# A função deve determinar cada dígito binário utilizando divisões sucessivas por 2.
# Não utilize:
# • as funções bin() ou format();
# • estruturas de repetição dentro da função;
# • listas para armazenar os restos;
# • variáveis globais.
# Depois, crie um programa principal que leia vários números inteiros. A leitura deve
# ser encerrada quando o usuário informar um número negativo. Para cada número
# válido, o programa deve exibir:
# • sua representação binária;
# • a quantidade de algarismos binários produzidos;
# • a quantidade de dígitos iguais a 1.
# A contagem de dígitos iguais a 1 também deve ser realizada por uma função recursiva.

def converter_binario(n):
    if n < 2:
        return str(n)
    return converter_binario(n // 2) + str(n % 2)

def contar_uns(binario):
    if not binario:
        return 0
    
    if binario[0] == "1":
        return 1 + contar_uns(binario[1:])
    
    return contar_uns(binario[1:])


while True:
    numero = int(input("Informe um número inteiro não negativo (ou negativo para sair): "))
    if numero < 0:
        break
        
    bin_str = converter_binario(numero)
    qtd_total = len(bin_str)
    qtd_uns = contar_uns(bin_str)
    
    print(f"Representação binária: {bin_str}")
    print(f"Quantidade de algarismos: {qtd_total}")
    print(f"Quantidade de dígitos iguais a 1: {qtd_uns}\n")
