"""
Exercício 1 Cabeçalho do atendimento
Crie um procedimento chamado exibir_cabecalho() que mostre na tela uma mensagem fixa de abertura do sistema de atendimento de uma loja.

A mensagem deve conter:

o nome da loja;
a frase "Sistema de Atendimento".
Depois de criar o procedimento, faça a chamada dele no programa principal.
"""

"""
Exercício 2 Identificação do cliente
Crie um procedimento chamado exibir_cliente(nome) que receba o nome de um cliente e exiba a mensagem:

Cliente: nome_informado
No programa principal:

leia o nome do cliente;
chame o procedimento passando esse valor.
"""

"""
Crie uma função chamada calcular_comissao(valor_venda) que receba o valor de uma venda e retorne a comissão correspondente a 5% desse valor.

No programa principal:

leia o valor da venda;
chame a função;
exiba o valor retornado.
"""

"""
Exercício 4 Cálculo do valor final com desconto
Crie uma função chamada calcular_valor_final(valor_produto, desconto) que receba:

o valor original de um produto;
o percentual de desconto concedido ao cliente.
A função deve retornar o valor final do produto após a aplicação do desconto.

No programa principal:

leia o valor do produto;
leia o percentual de desconto;
exiba o valor final calculado.
"""

def calcular_valor_final(valor_produto, desconto):
    valor_final = valor_produto - (valor_produto * (desconto / 100))
    return valor_final #return valor_produto * (1 - desconto / 100) 


def calcular_comissao(valor_venda):
    comissao =  (5 / 100) * valor_venda 
    return comissao

def exibir_cabecalho():
    print("MARISO")
    print("Sistema de Atendimento")

def exibir_cliente(nome):
    print(f"Cliente: {nome}")

exibir_cabecalho()

nome = input("Digite o nome do cliente: ")
exibir_cliente(nome)

valorVenda = float(input("Digite o valor da venda: "))
comissao = calcular_comissao(valorVenda)
print(comissao)

valor_produto = float(input("Digite o valor do produto: "))
desconto = int(input("Digite o valor do desconto (ex: 10): "))
valor_final = calcular_valor_final(valor_produto, desconto)
print(valor_final)



