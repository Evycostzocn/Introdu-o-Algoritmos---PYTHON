distancia = int(input("Digite a distância da viagem em km: "))
consumo = int(input("Digite o consumo do carro (km/l): "))
preco = float(input("Digite o preço do combustivel: "))

qtdLitros = distancia / consumo
custo = preco * qtdLitros

print(f"Planejamento de viagem\n-----------------------\nLitros necessários: {qtdLitros}\nCusto estimado: {custo:.2f}")