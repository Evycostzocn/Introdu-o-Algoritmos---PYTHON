# 19. Uma loja deseja representar seus pedidos utilizando composição de classes.
# Crie inicialmente uma classe chamada Produto, contendo os atributos privados:
# • código;
# • descrição;
# • preço unitário;
# • quantidade disponível em estoque.
# A classe deve possuir métodos para consultar seus dados, acrescentar unidades ao
# estoque e retirar unidades do estoque. Uma retirada somente pode ocorrer quando
# houver quantidade suficiente.
# Em seguida, crie uma classe chamada ItemPedido, contendo:
# • um objeto da classe Produto;
# • a quantidade solicitada.
# A classe deve possuir um método que calcule o subtotal do item.
# Por fim, crie uma classe chamada Pedido, contendo:
# • número do pedido;
# • nome do cliente;
# • uma lista de objetos da classe ItemPedido;
# • situação do pedido, inicialmente definida como "Aberto".
# Implemente na classe Pedido os métodos:
# • adicionar_item(produto, quantidade);
# • remover_item(codigo_produto);
# • calcular_total();
# • finalizar();
# • exibir_resumo().
# Ao finalizar um pedido, o estoque de cada produto deve ser reduzido. O pedido
# somente poderá ser finalizado se houver estoque suficiente para todos os itens. Caso
# um único item não possa ser atendido, nenhum estoque deverá ser alterado.
# Depois de finalizado, o pedido não poderá receber nem remover itens.
# No programa principal, crie diferentes produtos e pelo menos dois pedidos, incluindo
# uma tentativa de finalização sem estoque suficiente.

class Produto:
    def __init__(self, preco, codigo, quantidade_estoque, descricao):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco_unitario = preco
        self.__quantidade_estoque = quantidade_estoque
    
    def consultar(self):
        print(self.__codigo)
        print(self.__descricao)
        print(self.__preco_unitario)
        print(self.__quantidade_estoque)

    def acrescentar(self, quantidade_pedido):
        self.__quantidade_estoque += quantidade_pedido
    
    def retirar(self, quantidade_pedido):
        if quantidade_pedido <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade_pedido
            return True
        return False

    def consultar_preco(self):
        return self.__preco_unitario
    
    def consultar_codigo(self):
        return self.__codigo
    
    def consultar_estoque(self):
        return self.__quantidade_estoque
    
class ItemPedido:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade
    
    def calcular_subtotal(self):
        return self.__produto.consultar_preco() * self.__quantidade
    
    def get_produto(self):
        return self.__produto
    
    def get_quantidade(self):
        return self.__quantidade

class Pedido:
    def __init__(self, num_pedido, nome):
        self.__items = []
        self.__situacao = "Aberto"
        self.__num_pedido = num_pedido
        self.__nome = nome
    
    def adicionar_item(self, produto, quantidade):
        if self.__situacao != "Aberto":
            return
        item = ItemPedido(produto, quantidade)
        self.__items.append(item)
    
    def remover_item(self, codigo_produto):
        if self.__situacao != "Aberto":
            return
        for item in self.__items:
            if item.get_produto().consultar_codigo() == codigo_produto:
                self.__items.remove(item)
                break

    def calcular_total(self):
        total = 0
        for item in self.__items:
            total += item.calcular_subtotal()
        return total
    
    def finalizar(self):
        # nao sei ainda
        if self.__situacao != "Aberto":
            return False
        # verifica estoque
        for item in self.__items:
            produto = item.get_produto()
            quantidade = item.get_quantidade()
            if quantidade > produto.consultar_estoque():
                return False 
        for item in self.__items:
            produto = item.get_produto()
            quantidade = item.get_quantidade()
            produto.retirar(quantidade)
        self.__situacao = "Finalizado"
        return True    
    
    def exibir_resumo(self):
        # nao sei ainda
        print(f"Pedido: {self.__num_pedido}")
        print(f"Cliente: {self.__nome}")
        print(f"Situação: {self.__situacao}")
        print("Itens:")
        for item in self.__items:
            produto = item.get_produto()
            print(
                f"- {produto.consultar_codigo()} | "
                f"{item.get_quantidade()}x | "
                f"Subtotal: R$ {item.calcular_subtotal()}"
            )

        print(f"Total: R$ {self.calcular_total()}")


p1 = Produto(10.0, 101, 5, "Arroz")
p2 = Produto(5.0, 102, 2, "Feijão")
p3 = Produto(20.0, 103, 1, "Carne")


pedido1 = Pedido(1, "Evy")

pedido1.adicionar_item(p1, 2)
pedido1.adicionar_item(p2, 1)

# tentativa inválida (sem estoque suficiente depois)
pedido1.adicionar_item(p3, 2)

print("\n--- PEDIDO 1 ---")
print("Total:", pedido1.calcular_total())
print("Finalizando pedido 1:", pedido1.finalizar())
pedido1.exibir_resumo()

pedido2 = Pedido(2, "Evy")

pedido2.adicionar_item(p1, 1)
pedido2.adicionar_item(p2, 1)

print("\n--- PEDIDO 2 ---")
print("Total:", pedido2.calcular_total())
print("Finalizando pedido 2:", pedido2.finalizar())
pedido2.exibir_resumo()

print("\n--- ESTOQUE FINAL ---")
p1.consultar()
p2.consultar()
p3.consultar()