n = int (input () )
maior = n

if n == 0:
    print("valor invalido")
    exit()

while n != 0:
    if n > maior:
        maior = n
    n = int (input ())
print (maior)