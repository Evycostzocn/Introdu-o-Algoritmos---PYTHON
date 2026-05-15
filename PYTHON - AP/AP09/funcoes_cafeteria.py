def calcular_valores(valor1, valor2, taxa_servico = 10):

    subtotal = valor1 + valor2
    valorTaxa = subtotal * (taxa_servico / 100)
    totalPedido = subtotal + valorTaxa

    return subtotal, valorTaxa, totalPedido

def calcular_preco_cafe(preco_base, acrescimo = 0):

    return preco_base + acrescimo

def calcular_acompanhamento(preco, desconto = 0):

    return preco - (preco * (desconto / 100))

def resumo_item(nome, valor):
    valor_formatado = f"R$ {valor:.2f}"
    return nome, valor_formatado
