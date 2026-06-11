def zerar_negativos(medicoes):
    for i in range (len(medicoes)):
        if medicoes[i] < 0:
            medicoes[i] = 0

lista = [5, -2, 8, -1, 3]

listaO = lista.copy()

zerar_negativos(lista)

print(lista)
print(listaO)
