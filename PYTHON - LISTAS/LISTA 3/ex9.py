# O algoritmo de Euclides permite calcular o máximo divisor comum de dois números
# inteiros utilizando sucessivas operações de resto.
# Crie uma função recursiva chamada calcular_mdc(a, b) que utilize as seguintes regras:
# • quando b for igual a zero, o resultado será a;
# • caso contrário, o resultado será obtido por meio de uma nova chamada com os
# valores b e a % b.
# Por exemplo:
# calcular_mdc(48, 18) -> 6
# calcular_mdc(100, 25) -> 25
# calcular_mdc(17, 5) -> 1
# Depois, crie um programa principal que leia pares de números positivos até que o
# primeiro número informado seja zero. Para cada par, exiba:
# • o máximo divisor comum;
# • se os números são coprimos;
# • o mínimo múltiplo comum, calculado a partir do MDC.
# Dois números são considerados coprimos quando seu máximo divisor comum é igual
# a 1.

def calcular_mdc(a, b):
    if b == 0:
        return a
    else:
        return calcular_mdc(b, a % b)

while True:
    a = int(input("Valor de a: "))
    b = int(input("Valor de b: "))

    if a == 0:
        print("programa encerrado!")
        exit()

    mdc = calcular_mdc(a, b)

    print(f"MDC: {mdc}")

    if mdc == 1:
        print("COPRIMOS")
    
    mmc = (a * b) // mdc
    print(f"MMC: {mmc}")