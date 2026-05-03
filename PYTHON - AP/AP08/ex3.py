"""
Exercício 11 Cálculo da inscrição com taxa padrão
Crie uma função chamada calcular_inscricao(valor_base, taxa=10) que receba:

o valor base da inscrição;
a taxa percentual de serviço, que por padrão será 10.
A função deve retornar o valor total da inscrição.

No programa principal:

leia o valor base;
chame a função uma vez sem informar a taxa;
chame a função outra vez informando uma taxa diferente;
exiba os dois resultados.
"""

"""
Exercício 12 Conversão do tempo de prova
Crie uma função chamada converter_tempo(total_segundos) que receba o tempo total de prova em segundos e retorne três valores:

horas;
minutos;
segundos restantes.
No programa principal:

leia o tempo total em segundos;
chame a função;
exiba os valores retornados.
"""

"""
Exercício 13 Resumo do resultado do participante
Utilize a função do exercício anterior para criar uma nova função chamada gerar_resumo_tempo(nome, total_segundos).

Essa nova função deve:

chamar a função converter_tempo(total_segundos);
receber os valores retornados;
montar e retornar uma frase no formato:
Participante NOME: H hora(s), M minuto(s) e S segundo(s).
No programa principal:

leia o nome do participante;
leia o tempo em segundos;
chame a função;
exiba a frase retornada.
"""

"""
Exercício 14 Faixa de números de peito
Em uma corrida, a organização deseja identificar rapidamente quantos números de peito pares existem em uma faixa numérica, pois eles serão destinados a uma categoria específica.

Crie duas funções:
a) eh_par(numero)
Deve retornar True se o número for par e False caso contrário.
b) contar_pares_faixa(inicio, fim)
Deve percorrer todos os números do intervalo de inicio até fim, inclusive, e contar quantos deles são pares.
Importante: dentro da função contar_pares_faixa, a verificação deve ser feita chamando a função eh_par(numero).
No programa principal:
leia o início e o fim da faixa;
exiba a quantidade de números pares.
"""

"""
Exercício 15 Fechamento de inscrições e resultados da corrida
A escola está organizando uma corrida estudantil e precisa de um programa para registrar, de forma rápida, os dados de vários participantes. O objetivo é evitar repetir manualmente os mesmos cálculos e formatações para cada novo inscrito.

Escreva um programa que processe os dados de N participantes. Para cada participante, o programa deve:

ler o nome;
ler o valor base da inscrição;
calcular o valor total da inscrição com taxa;
ler o tempo da prova em segundos;
converter esse tempo;
gerar um resumo textual do resultado;
ler o início e o fim de uma faixa de números de peito associada ao participante;
calcular quantos números pares existem nessa faixa;
exibir um resumo organizado daquele participante.
Entradas:

Para cada um dos N participantes:

nome;
valor base da inscrição;
tempo da prova em segundos;
início da faixa;
fim da faixa.
Saídas esperadas:

Para cada participante, o programa deve mostrar:

nome;
valor total da inscrição;
tempo convertido;
frase resumida com o tempo;
quantidade de números pares na faixa informada.
"""

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
    # Poderia resumir essa função em: return numero % 2 == 0

def contar_pares_faixa(inicio, fim):
    countPares = 0
    for i in range(inicio, fim + 1):
        if eh_par(i):
            countPares += 1
    return countPares
        
def gerar_resumo_tempo(nome, total_segundos):
    horas, minutos, segundos_restantes = converter_tempo(total_segundos)
    print(f"NOME: {nome} → {horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s)")
  
def calcular_inscricao(valor_base, taxa = 10):
    valor_total = valor_base + (valor_base * (taxa / 100))
    return valor_total

def converter_tempo(total_segundos):
    horas = total_segundos // 3600
    segundos_restantes = total_segundos % 3600
    minutos = segundos_restantes // 60
    segundos_restantes %= 60
    return horas, minutos, segundos_restantes

valorBase = float(input("Digite um valor: "))
novoValor = calcular_inscricao(valorBase)
novoValor2 = calcular_inscricao(valorBase, 10)

print(novoValor)
print(novoValor2)

while True:
    nome = input("Digite o nome do participante: ")
    tempoTotal = int(input("Digite o tempo total em segundos: "))
    gerar_resumo_tempo(nome, tempoTotal)

    inicio = int(input("Digite o início da faixa: "))
    fim = int(input("Digite o fim da faixa: "))
    qtdPares = contar_pares_faixa(inicio, fim)
    print(f"Quantidade de números pares: {qtdPares}")

    continuar = input("Deseja continuar o programa (s/n): ")
    if continuar != "s" and continuar != "S":
        break

