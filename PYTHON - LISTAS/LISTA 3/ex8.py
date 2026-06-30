# 8. Crie uma função recursiva chamada soma_digitos(numero) que receba um
# número inteiro não negativo e retorne a soma de seus algarismos.
# Por exemplo:
# soma_digitos(4725) -> 18
# soma_digitos(90) -> 9
# soma_digitos(7) -> 7
# A função deve obter o último algarismo utilizando o resto da divisão por 10 e reduzir
# o número por meio da divisão inteira por 10.
# Não utilize:
# • estruturas de repetição dentro da função;
# • conversão do número para string;
# • listas ou variáveis globais.
# No programa principal, leia vários números inteiros não negativos. A leitura deve
# ser encerrada quando o usuário informar um número negativo. Para cada número
# válido, exiba a soma de seus algarismos.

def soma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) * soma_digitos(numero // 10)

while True:
    num = int(input("Numero: "))

    if num < 0:
        print("Numeros negativos param o programa!")
        exit()
    
    print(soma_digitos(num))