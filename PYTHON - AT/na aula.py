def contar_digitos(valor):
    if valor < 10:
        return 1
    else:
        valor // 10 = valor
        return 1 + contar_digitos(valor)
count = 0
valor = 4972    
print(contar_digitos(valor))