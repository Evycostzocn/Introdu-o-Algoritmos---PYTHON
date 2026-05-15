import funcoes_cafeteria as fc
def main ():
    nome_cafe = input("Nome do café: ")
    preco_base = float(input("Digite o preço do café: "))
    acrescimo = float(input("Acréscimo do tamanho: "))

    nome_acompanhamento = input("Digite o nome do acompanhamento: ")
    preco_acompanhamento = float(input("Digite o preço do acompanhamento: "))
    desconto = float(input("Digite o valor do desconto: "))

    taxa_servio = float(input("Digite o valor da taxa de serviço: "))

    # calculos usando as funções da biblioteca importada

    valor_cafe = fc.calcular_preco_cafe(preco_base, acrescimo)
    valor_acompanhamento = fc.calcular_acompanhamento(preco_acompanhamento, desconto)

    # resumos dos itens pedidos

    cafe_nome, cafe_valor = fc.resumo_item(nome_cafe, valor_cafe)

    acomp_nome, acomp_valor = fc.resumo_item(nome_acompanhamento, valor_acompanhamento)

    # valores totais

    subtotal, taxa, total = fc.calcular_valores(valor_cafe, valor_acompanhamento, taxa_servio)

    print("\n============= RESUMO DO PEDIDO =================")
    print(f"{cafe_nome}: {cafe_valor}")
    print(f"{acomp_nome}: {acomp_valor}")
    print(f"\nSubtotal: R$ {subtotal:.2f}")
    print(f"Taxa de serviço: R$ {taxa:.2f}")
    print(f"Total final: R$ {total:.2f}")

if __name__ == "__main__":
    main()
