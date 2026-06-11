"""
Faça uma função calcular_bonus(pontos) para um sistema de RH. Se a pontuação for maior que 50, o bônus é de R$ 100,00; caso contrário, R$ 10,00. Em
seguida, crie um programa que leia a pontuação de N funcionários, armazene-os em
uma lista e use a função para substituir a pontuação na lista pelo valor do bônus
recebido, imprimindo a lista final e o total pago."""

def calcular_bonus(pontos):
    if pontos > 50:
        return 100
    else:
        return 10

lista = []
soma = 0

while True:
    pontos_funcionario = float(input("Digite a pontuação do funcionario, 0 para sair: "))
    if pontos_funcionario == 0:
        break
    lista.append(pontos_funcionario)

for i in range (len(lista)):
    bonus = calcular_bonus(lista[i])
    lista[i] = bonus
    soma += bonus

print(f"Lista final: {lista}")
print(f"Total pago: R$ {soma:.2f}")



