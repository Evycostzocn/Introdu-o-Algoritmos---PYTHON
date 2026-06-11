"""
Uma cooperativa agrícola possui um silo com capacidade limitada de sementes. Crie
um procedimento processar_pedidos(estoque_inicial) que leia continuamente o peso desejado pelos agricultores. Se o valor for maior que o estoque, o
pedido é negado. Caso contrário, o estoque é reduzido. O procedimento deve encerrar quando o estoque zerar ou quando um pedido negativo for inserido, exibindo
o total de agricultores atendidos e a sobra no silo.
"""

def processar_pedidos(estoque_inicial):
    novo_estoque = estoque_inicial
    agricultores_atendidos = 0
    while True:
        peso = int(input("peso desejado: "))
        if peso < 0:
            break
        if peso > novo_estoque:
            print("pedido negado!")
            continue
        else:
            novo_estoque -= peso
            agricultores_atendidos += 1
            if novo_estoque == 0:
                break
    return novo_estoque, agricultores_atendidos


estoque = int(input("valor do estoque: "))
estoque_final, total = processar_pedidos(estoque)
sobra = estoque - estoque_final

print(f"Sobra no silo: {estoque_final}")
print(f"Quantidade de agricultores atentidos: {total}")

