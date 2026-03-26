"""
Exercício 7 Sistema de classificação em uma competição
Uma competição escolar de programação classifica participantes com base em:

pontuação obtida
tempo gasto na prova
O programa deve ler:

pontuação total do participante
tempo total gasto (em minutos)
Classificação:

pontuação ≥ 90 → Ouro
pontuação ≥ 70 → Prata
pontuação ≥ 50 → Bronze
caso contrário → sem medalha
Regra adicional:

Se o participante obtiver Ouro e terminar a prova em menos de 120 minutos, ele recebe:

Participante destaque da competição
O programa deve mostrar:

a classificação obtida
e, se aplicável, o título de destaque"""

pontuacao = int(input("Pontuação: "))
tempo = int(input("Tempo (min): "))

if pontuacao >= 90 and tempo <= 120:
    print("Ouro\nParticipante destaque")
elif pontuacao >= 90:
    print("Ouro.")
elif pontuacao >= 70 and pontuacao < 90:
    print("Prata.")
else:
    print("Bronze.")

