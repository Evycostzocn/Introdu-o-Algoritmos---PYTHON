# 1. Um laboratório mantém o arquivo texto leituras.txt, contendo medições realizadas por diferentes sensores. Cada linha válida do arquivo possui o seguinte
# formato:
# codigo_sensor;data;temperatura
# Por exemplo:
# S01;10/06/2026;24.5
# S02;10/06/2026;27.3
# S01;11/06/2026;26.0
# S03;11/06/2026;erro
# S02;12/06/2026;28.1
# Desenvolva um programa que leia o arquivo e produza um relatório contendo, para
# cada sensor:
# • a quantidade de medições válidas;
# • a menor temperatura registrada;
# • a maior temperatura registrada;
# • a temperatura média.
# 1
# Linhas que não possuam exatamente três campos ou cuja temperatura não possa
# ser convertida para um número real devem ser consideradas inválidas.
# Ao final, o programa deve:
# • exibir a quantidade total de linhas inválidas;
# • identificar o sensor que apresentou a maior temperatura entre todas as medições;
# • gravar os resultados no arquivo relatorio_sensores.txt.
# O relatório deve apresentar um sensor por linha. Não considere que os códigos dos
# sensores sejam previamente conhecidos.

with open("leituras.txt", "r") as arq:
    linhas_invalidas = 0
    sensores = {}

    for linha in arq:
        partes = linha.strip().split(";")
        if len(partes) != 3:
            linhas_invalidas += 1 
            continue

        codigo = partes[0]
        temperatura = partes[2]

        try:
            valorTemperatura = float(temperatura)
        except ValueError:
            linhas_invalidas += 1
            continue
    
        if codigo not in sensores:
            sensores[codigo] = []
        sensores[codigo].append(valorTemperatura)

    maior_temperatura_geral = -999999
    sensor_maior = ""

with open("relatorio_sensores.txt", "w") as relatorio:

    for sensor, temperaturas in sensores.items():
        maior_sensor = max(temperaturas)

        if maior_sensor > maior_temperatura_geral:
            maior_temperatura_geral = maior_sensor
            sensor_maior = sensor

        print(f"Sensor: {sensor}")
        print(f"Quantidade: {len(temperaturas)}")
        print(f"Menor: {min(temperaturas)}")
        print(f"Maior: {maior_sensor}")
        media = sum(temperaturas) / len(temperaturas)
        print(f"Média: {media:.2f}")
        print("\n")
    
        relatorio.write(f"Sensor: {sensor}\n")
        relatorio.write(f"Quantidade: {len(temperaturas)}\n")
        relatorio.write(f"Maior temperatura: {maior_sensor}\n")
        relatorio.write("\n")

    print(f"Sensor com maior temperatura: {sensor_maior}")
    print(f"Maior temperatura registrada: {maior_temperatura_geral}")
    print(f"Linhas inválidas: {linhas_invalidas}")


