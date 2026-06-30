# 5. Crie uma função recursiva chamada potencia(base, expoente) que receba dois números inteiros positivos e 
# retorne o valor de base elevado a expoente.
# Por exemplo:
# potencia(2,0) -> 1
# potencia(4,1) -> 4
# potencia(2,10) -> 1024

def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)
    
base = int(input("base: "))
expoente = int(input("expoente: "))

pot = potencia(base, expoente)
print(pot)
