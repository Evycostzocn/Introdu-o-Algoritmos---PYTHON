# 23. Crie uma classe chamada Produto para representar um produto armazenado em
# uma loja.
# A classe deve possuir os atributos:
# • código;
# • nome;
# • preço unitário;
# • quantidade em estoque.
# Implemente um construtor e os seguintes métodos:
# • adicionar_estoque(quantidade);
# • retirar_estoque(quantidade);
# • alterar_preco(novo_preco);
# • calcular_valor_estoque();
# • exibir_produto().
# A classe deve impedir:
# • preços menores ou iguais a zero;
# • quantidades negativas;
# • retiradas superiores à quantidade disponível.
# No programa principal, crie uma lista com cinco objetos da classe Produto. Depois,
# exiba:
# • os dados de todos os produtos;
# • o produto com maior quantidade em estoque;
# • o produto com maior valor financeiro total em estoque;
# • o valor total de todos os produtos armazenados.

class Produto:
    def __init__(self, codigo, nome, preco_un, quantidade_estoque):
        self.codigo = codigo
        self.nome = nome
        self.quantidade_estoque = quantidade_estoque

        if preco_un <= 0:
            self.preco_un = 0
        else:
            self.preco_un = preco_un

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade_estoque += quantidade
        else:
            return False

        return self.quantidade_estoque

    def quantidade_no_estoque(self):
        return self.quantidade_estoque

    def retirar_estoque(self, quantidade):
        if quantidade < 0 or quantidade > self.quantidade_estoque:
            return False

        self.quantidade_estoque -= quantidade
        return self.quantidade_estoque

    def alterar_preco(self, novo_preco):
        if novo_preco <= 0:
            return False

        self.preco_un = novo_preco
        return self.preco_un

    def calcular_valor_estoque(self):
        return self.preco_un * self.quantidade_estoque

    def exibir_produto(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco_un:.2f}")
        print(f"Quantidade: {self.quantidade_estoque}")
        print("-" * 30)


p1 = Produto(1, "Teclado", 150.00, 10)
p2 = Produto(2, "Mouse", 10.00, 7)
p3 = Produto(3, "Notebook", 1500.00, 7)
p4 = Produto(4, "Monitor", 450.00, 3)
p5 = Produto(5, "MousePad", 50.00, 20)

lista = [p1, p2, p3, p4, p5]

print("TODOS OS PRODUTOS")
print("-" * 30)

for produto in lista:
    produto.exibir_produto()

# Produto com maior quantidade em estoque
maior = p1

if p2.quantidade_no_estoque() > maior.quantidade_no_estoque():
    maior = p2

if p3.quantidade_no_estoque() > maior.quantidade_no_estoque():
    maior = p3

if p4.quantidade_no_estoque() > maior.quantidade_no_estoque():
    maior = p4

if p5.quantidade_no_estoque() > maior.quantidade_no_estoque():
    maior = p5

print("\nPRODUTO COM MAIOR QUANTIDADE EM ESTOQUE")
maior.exibir_produto()

# Produto com maior valor financeiro em estoque
maior_valor = p1

if p2.calcular_valor_estoque() > maior_valor.calcular_valor_estoque():
    maior_valor = p2

if p3.calcular_valor_estoque() > maior_valor.calcular_valor_estoque():
    maior_valor = p3

if p4.calcular_valor_estoque() > maior_valor.calcular_valor_estoque():
    maior_valor = p4

if p5.calcular_valor_estoque() > maior_valor.calcular_valor_estoque():
    maior_valor = p5

print("\nPRODUTO COM MAIOR VALOR EM ESTOQUE")
maior_valor.exibir_produto()

# Valor total de todos os produtos em estoque
valor_total = 0

for produto in lista:
    valor_total += produto.calcular_valor_estoque()

print(f"Valor total do estoque: R$ {valor_total:.2f}")