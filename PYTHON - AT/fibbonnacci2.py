numero = int(input("digite numero fibbonnacci: "))
atual = 1
anterior = 0
soma = 0


for i in range (1, numero + 1):
    print(anterior)
    soma = anterior + atual
    anterior = atual
    atual = soma
    

    
