# Variáveis / Entrada de dados

potencia = float(input("Digite a potência do aparelho: "))
horasDia = int(input("Digite as horas que o aparelho é utilizado: "))
diasMes = int(input("Digite a quantidade de dias em que é usado no mês: "))
preco = float(input("Digite o preço da energia: "))

consumoDiario = (potencia * horasDia) / 1000
consumoMensal = consumoDiario * diasMes
custoMensal = consumoMensal * preco

print(f"RELATÓRIO DE CONSUMO\n--------------------\nConsumo diário (kwh): {consumoDiario:.2f}\nConsumo mensal (kwh): {consumoMensal}\nCusto mensal: {custoMensal}")
