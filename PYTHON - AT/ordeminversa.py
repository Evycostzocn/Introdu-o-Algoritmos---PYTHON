numeros = []

for i in range (5):
    num = float(input(f"Digite o {i + 1} numero: "))
    numeros.append(num)

i = len(numeros) - 1
while i >= 0:
    print(numeros[i])
    i -= 1