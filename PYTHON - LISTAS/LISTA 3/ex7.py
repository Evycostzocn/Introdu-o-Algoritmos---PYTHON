# 7. Crie uma função recursiva chamada existe(lista, valor, i) que verifique se valor
# aparece na lista a partir da posição i. Se o valor existir na lista, a função retorna
# True, e caso contrário, retorna False.
# Por exemplo:
# existe([1,2,4,6,0],2,0) -> True
# existe([1,2,4,6,0],2,9) -> False

def existe(lista, valor, i):
    if i >= len(lista):
        return False
    
    if valor == lista[i]:
        return True
    
    else:
        return existe(lista, valor, i + 1)
    
lista = [1,2,4,6,0]
valor = 2
i = 0

print(existe(lista,valor,i))