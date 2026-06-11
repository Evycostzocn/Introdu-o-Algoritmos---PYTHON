def soma_ate(n, atual = 1):
    if atual > n:
        return 0
    
    return atual + soma_ate(n, atual + 1)

n = int(input("n: "))

soma = soma_ate(n)

print(soma)