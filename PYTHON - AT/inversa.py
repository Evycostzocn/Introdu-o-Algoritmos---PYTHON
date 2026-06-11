valores = []

for i in range(5):
    num = int(input("n: "))
    valores.append(num)

i = len(valores) - 1
arquivo = open("inverso.txt", "w", encoding="utf-8")

while i >= 0:
    print(valores[i])
    arquivo.write(str(valores[i]) + "\n")
    i -= 1
arquivo.close()
