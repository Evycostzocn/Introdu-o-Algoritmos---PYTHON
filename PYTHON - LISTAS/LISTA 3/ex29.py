# 29. Uma plataforma de entrega de refeições funciona da seguinte maneira:
# Cada restaurante possui nome, endereço e um cardápio. O cardápio é
# formado por produtos, e cada produto possui código, descrição e preço.
# Um cliente possui nome, telefone e endereço de entrega. Para realizar uma
# compra, o cliente cria um pedido e adiciona produtos do cardápio. Para
# cada produto adicionado, o pedido deve armazenar também a quantidade
# solicitada.
# O pedido deve calcular seu valor total, permitir a remoção de itens e
# possuir uma situação, que pode ser “Aberto”, “Confirmado”, “Em preparação”, “Saiu para entrega” ou “Entregue”. Um pedido confirmado não
# pode receber novos itens.
# Faça a modelagem orientada a objetos do problema.
# Sua resposta deve identificar:
# • as classes;
# • os atributos de cada classe;
# • os métodos de cada classe;
# • quais relacionamentos representam associação;
# • quais relacionamentos representam composição;
# • qual classe deve calcular o subtotal de um produto com determinada quantidade;
# • qual classe deve calcular o valor total da compra.
# Depois, implemente as classes e crie um programa principal que:
# • crie um restaurante e seu cardápio;
# • crie dois clientes;
# • registre pedidos com diferentes itens;
# • altere as situações dos pedidos;
# • tente adicionar um item a um pedido já confirmado;
# • exiba um resumo completo de cada pedido.

# MODELAGEM DO SISTEMA
# Classes, Atributos e Métodos
# Produto

# Atributos: codigo, descricao, preco.

# Métodos: Getters básicos.

# Restaurante

# Atributos: nome, endereco, cardapio (lista de objetos Produto).

# Métodos: adicionar_ao_cardapio(produto).

# Cliente

# Atributos: nome, telefone, endereco_entrega.

# Métodos: Nenhum específico além do construtor.

# ItemPedido

# Atributos: produto (objeto Produto), quantidade.

# Métodos: calcular_subtotal().

# Pedido

# Atributos: cliente (objeto Cliente), restaurante (objeto Restaurante), itens (lista de objetos ItemPedido), situacao (string).

# Métodos: adicionar_item(produto, quantidade), remover_item(codigo_produto), alterar_situacao(nova_situacao), calcular_total(), exibir_resumo().

# Mapeamento de Relacionamentos
# Associação: * Pedido e Cliente (O pedido conhece o cliente que o fez).

# Pedido e Restaurante (O pedido sabe de qual restaurante foi feito).

# ItemPedido e Produto (O item do pedido aponta para o produto do cardápio).

# Composição:

# Restaurante e Produto (O cardápio é composto por produtos do restaurante).

# Pedido e ItemPedido (Os itens pertencem exclusivamente àquele pedido. Se o pedido for deletado, a lista de itens deixa de existir).

# Responsabilidades de Cálculo
# Subtotal de um produto com determinada quantidade: Classe ItemPedido (multiplica o preço do produto associado pela quantidade).

# Valor total da compra: Classe Pedido (percorre sua lista de ItemPedido somando o subtotal de cada um).

# --- CLASSE PRODUTO ---
class Produto:
    def __init__(self, codigo, descricao, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = float(preco)


# --- CLASSE RESTAURANTE ---
class Restaurante:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cardapio = []

    def adicionar_ao_cardapio(self, produto):
        self.cardapio.append(produto)


# --- CLASSE CLIENTE ---
class Cliente:
    def __init__(self, nome, telefone, endereco_entrega):
        self.nome = nome
        self.telefone = telefone
        self.endereco_entrega = endereco_entrega


# --- CLASSE ITEM PEDIDO ---
class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.produto.preco * self.quantidade


# --- CLASSE PEDIDO ---
class Pedido:
    def __init__(self, cliente, restaurante):
        self.cliente = cliente
        self.restaurante = restaurante
        self.itens = []
        self.situacao = "Aberto"

    def adicionar_item(self, produto, quantidade):
        if self.situacao != "Aberto":
            print(f"Erro: Não é possível adicionar itens. O pedido está '{self.situacao}'.")
            return False
        
        self.itens.append(ItemPedido(produto, quantidade))
        return True

    def remover_item(self, codigo_produto):
        if self.situacao != "Aberto":
            print(f"Erro: Não é possível remover itens. O pedido está '{self.situacao}'.")
            return False
            
        for item in self.itens:
            if item.produto.codigo == codigo_produto:
                self.itens.remove(item)
                return True
        return False

    def alterar_situacao(self, nova_situacao):
        situacoes_validas = ["Aberto", "Confirmado", "Em preparação", "Saiu para entrega", "Entregue"]
        if nova_situacao in situacoes_validas:
            self.situacao = nova_situacao
        else:
            print("Erro: Situação inválida.")

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.itens)

    def exibir_resumo(self):
        print(f"\n================ RECON DE PEDIDO ================")
        print(f"Restaurante: {self.restaurante.nome}")
        print(f"Cliente: {self.cliente.nome} | Telefone: {self.cliente.telefone}")
        print(f"Endereço de Entrega: {self.cliente.endereco_entrega}")
        print(f"Situação do Pedido: {self.situacao}")
        print("-" * 49)
        for item in self.itens:
            print(f" {item.quantidade}x {item.produto.descricao:<20} (R$ {item.produto.preco:.2f} un) -> Subtotal: R$ {item.calcular_subtotal():.2f}")
        print("-" * 49)
        print(f"TOTAL DO PEDIDO: R$ {self.calcular_total():.2f}")
        print("=================================================")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # 1. Criar restaurante e cardápio
    restaurante = Restaurante("Burger House", "Av. Central, 100")
    p1 = Produto(101, "Combo Cheeseburger", 35.00)
    p2 = Produto(102, "Batata Frita M", 12.50)
    p3 = Produto(103, "Refrigerante Lata", 6.00)
    restaurante.adicionar_ao_cardapio(p1)
    restaurante.adicionar_ao_cardapio(p2)
    restaurante.adicionar_ao_cardapio(p3)

    # 2. Criar dois clientes
    c1 = Client_1 = Cliente("Marcos Oliveira", "9999-0001", "Rua das Flores, 45")
    c2 = Client_2 = Cliente("Juliana Reis", "9999-0002", "Alamedas das Palmeiras, 112")

    # 3. Registrar pedidos com diferentes itens
    pedido1 = Pedido(c1, restaurante)
    pedido1.adicionar_item(p1, 2)  # 2 Combos
    pedido1.adicionar_item(p2, 1)  # 1 Batata

    pedido2 = Pedido(c2, restaurante)
    pedido2.adicionar_item(p1, 1)  # 1 Combo
    pedido2.adicionar_item(p3, 2)  # 2 Refringentes

    # 4. Alterar as situações dos pedidos
    pedido1.alterar_situacao("Confirmado")
    pedido1.alterar_situacao("Em preparação")
    
    # 5. Tentar adicionar um item a um pedido já confirmado (Deve dar erro)
    print("--- Tentativa inválida de inserção de dados ---")
    pedido1.adicionar_item(p3, 1) 

    # Movimentando o pedido 2 de forma limpa
    pedido2.alterar_situacao("Confirmado")

    # 6. Exibir resumo completo de cada pedido
    pedido1.exibir_resumo()
    pedido2.exibir_resumo()