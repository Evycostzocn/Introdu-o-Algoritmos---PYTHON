"""
Peça uma base e um expoente inteiro não negativo ao usuário e calcule a potência
manualmente, sem usar operador de exponenciação, utilizando um for.
"""
base = int(input("base: "))
expoente = int(input("expoente: "))
potencia = 1
for i in range(1, expoente + 1):
    potencia *= base
print(f"potência: {potencia}")