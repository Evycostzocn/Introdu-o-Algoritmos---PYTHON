# 4. Crie uma função recursiva chamada soma_ate(n) que receba um número inteiro
# positivo n e retorne a soma de todos os números de 1 até n.
# Por exemplo:
# soma_ate(5) -> 15
# soma_ate(3) -> 6
# soma_ate(0) -> 0


def soma_ate(n):
    if n == 0: # if n <= 0
        return 0
    else:
        return n + soma_ate(n - 1)
    
n = int(input("n: "))
soma = soma_ate(n)

print(soma)