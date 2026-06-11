def potencia(base, expoente):
    if expoente == 0:
        return 1

    return base * potencia(base, expoente - 1)

base = int(input("base: "))
expoente = int(input("expoente: "))

potencia = potencia(base, expoente)

print(potencia)