"""
Fernanda, Francisca e Flávia são três irmãs. Sabe-se que Fernanda nasceu antes
de Francisca e Flávia nasceu depois de Francisca. Faça um programa que leia
3 três números inteiros correspondentes às idades das irmãs (em qualquer ordem) e
imprima a idade de Francisca.
"""
idade = int(input("Idade da irmã: "))

maisVelha = idade
cacula = idade
irmaMeio = idade
soma = idade

for i in range(1, 3):
    idade = int(input("Idade da irmã: "))

    if idade > maisVelha:
        maisVelha = idade
    elif idade < cacula:
        cacula = idade
    
    soma += idade 

irmaMeio = soma - maisVelha - cacula
print(f"Idade da Francisca: {irmaMeio}")