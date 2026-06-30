# 6. Crie uma função recursiva chamada contar_digitos(n) que receba um número inteiro
# positivo n e retorne a quantidade de dígitos desse número.
# Por exemplo:
# soma_digitos(4725) -> 4
# soma_digitos(90) -> 2
# soma_digitos(7) -> 1

def contar_digitos(n):
    if n < 10:
        return 1

    return 1 + contar_digitos(n // 10)
    
n = int(input("n: "))
qtd_digitos = contar_digitos(n)
print(qtd_digitos)