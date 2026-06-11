def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)

n = int(input("n: "))

numdig = contar_digitos(n)

print(numdig)