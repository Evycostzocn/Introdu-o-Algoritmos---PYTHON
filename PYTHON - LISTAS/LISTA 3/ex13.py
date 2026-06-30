# 13. Crie uma função recursiva chamada
# eh_primo(numero, divisor)
# que determine se um número inteiro é primo.
# A chamada inicial deve utilizar o divisor 2:
# eh_primo(numero, 2)
# A função deve utilizar as seguintes regras:
# • números menores que 2 não são primos;
# • se algum divisor produzir resto igual a zero, o número não é primo;
# • se o quadrado do divisor atual for maior que o número, nenhum outro divisor
# precisa ser testado e o número é primo;
# • caso contrário, a função deve testar o próximo divisor.
# Não utilize estruturas de repetição dentro da função.
# No programa principal, leia dois números inteiros positivos, representando o início
# e o final de um intervalo. Utilize a função recursiva para verificar cada número do
# intervalo e exiba todos os números primos encontrados, além da quantidade total
# de primos.

def eh_primo(numero, divisor):
    if numero < 2:
        return False
    
    if divisor ** 2 > numero:
        return True
    
    if numero % divisor == 0:
        return False
    
    return eh_primo(numero, divisor + 1)

inicio = int(input("inicio: "))
fim = int(input("fim: "))

count_primo = 0

for i in range(inicio, fim + 1):
    if eh_primo(i, 2):
        print(f"numero: {i}")
        count_primo += 1

print(f"quantidade de primos: {count_primo}")

