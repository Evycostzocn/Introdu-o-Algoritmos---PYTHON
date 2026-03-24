n = int (input("n: "))

atual = 1
anterior = 0 
soma = 0

while n > 0:
    print(anterior)
    soma = atual + anterior
    anterior = atual
    atual = soma
    n = n - 1