"""
Uma provedora de nuvem cobra por hora de uso de instâncias de servidor. Crie uma
função calcular_fatura(horas) que aplique as seguintes regras: as primeiras
100 horas custam R$ 5,00/hora; de 101 a 500 horas, o custo cai para R$ 4,00/hora
para as horas excedentes; acima de 500 horas, o custo cai para R$ 2,50/hora para
as horas excedentes. Faça um programa que leia o ID do cliente e horas consumidas
até que o ID seja 0. Imprima a fatura de cada cliente e o faturamento total da
empresa.
"""

def calcular_fatura(horas):
    valor_fatura = 0
    if horas <= 100:
        valor_fatura = horas * 5
    elif horas <= 500:
        valor_fatura = 100 * 5 + ((horas - 100) * 4)
    else:
        valor_fatura = (100 * 5) + (400 * 4) + ((horas - 500) * 2.5)
    
    return valor_fatura

faturamento_total = 0

while True:
    id_cliente = int(input("ID do cliente: "))

    if id_cliente == 0:
        break

    else:
        nome = input("Nome do cliente: ")
        horas = int(input("Horas consumidas: "))

        valor_fatura = calcular_fatura(horas)
        print(f"Cliente: {nome} | Valor da fatura: R$ {valor_fatura:.2f}")

        faturamento_total += valor_fatura

print(f"Faturamento total da empresa: R$ {faturamento_total:.2f}")

