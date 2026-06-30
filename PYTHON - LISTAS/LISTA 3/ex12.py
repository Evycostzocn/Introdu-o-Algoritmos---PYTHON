# 12. Crie uma função recursiva chamada multiplicar(a, b) que calcule o produto
# de dois números inteiros sem utilizar o operador de multiplicação.
# A multiplicação deve ser realizada por meio de somas ou subtrações sucessivas. A
# função deve tratar corretamente os seguintes casos:
# • os dois números são positivos;
# • apenas um dos números é negativo;
# • os dois números são negativos;
# • um dos números é igual a zero.
# Por exemplo:
# multiplicar(5, 4) -> 20
# multiplicar(5, -4) -> -20
# multiplicar(-5, 4) -> -20
# multiplicar(-5, -4) -> 20
# multiplicar(8, 0) -> 0
# Não utilize:
# • o operador *;
# • estruturas de repetição dentro da função;
# • conversões para string;
# • variáveis globais.
# No programa principal, leia diferentes pares de valores e compare o resultado produzido pela função recursiva com o resultado esperado.

def multiplicar(a, b):
    if b == 0:
        return 0
    elif b < 0:
        return - multiplicar(a, abs(b))
    else:
        return a + multiplicar(a, b - 1)

while True:
    a = int(input("a: "))
    b = int(input("b: "))

    if a == 0 and b == 0:
        print("programa encerrado!")
        break

    resultado = multiplicar(a, b)
    print(f"resultado: {resultado}")