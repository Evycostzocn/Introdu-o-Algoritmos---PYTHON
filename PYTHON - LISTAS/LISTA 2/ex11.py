"""
 Um drone de entregas precisa validar suas condições antes de decolar. Crie uma
função autorizar_voo(bateria, velocidade_vento) que retorne True
se a bateria for maior que 15% e o vento for menor que 30 km/h. O programa
principal deve ler os dados de 5 etapas de checagem. Em cada etapa, a bateria cai
2%. Se o voo for proibido em qualquer etapa, a função deve acionar um alerta e o
programa deve abortar a missão, indicando em qual etapa ocorreu a falha."""

def autorizar_voo(bateria, velocidade_vento):
    if bateria > 15 and velocidade_vento < 30:
        return True
    else:
        return False

vento = float(input("Velocidade do vento em km/h (ex: 20): "))
bateria = float(input("Carga da bateria em % (ex: 77): "))
bateriaFinal = bateria

for i in range(5):
    bateriaFinal = bateriaFinal - (bateriaFinal * (2 / 100))
    vooAutorizado = autorizar_voo(bateriaFinal, vento)
    if not vooAutorizado:
        print("ALERTA!")
        print(f"FALHA NA ETAPA {i + 1}")
        print("!!! MISSÃO SERÁ ABORTADA !!!")
        exit()
    else:
        print(f"Etapa {i + 1}: VOO AUTORIZADO")
        print(f"Etapa {i+ 1}: bateria = {bateriaFinal:.2f}%")

