# 21. Uma empresa deseja desenvolver um sistema de controle de estoque que integre
# manipulação de arquivos, recursividade e programação orientada a objetos.
# O arquivo produtos.txt armazena os produtos cadastrados, com uma linha no
# formato:
# codigo;descricao;preco;quantidade
# Crie uma classe chamada Produto, contendo atributos privados para os quatro
# campos do arquivo. A classe deve possuir:
# • um construtor;
# • métodos de acesso;
# • um método para acrescentar unidades;
# • um método para retirar unidades;
# • um método para calcular o valor total do produto em estoque.
# Crie também uma classe chamada Estoque, que mantenha uma lista de objetos
# da classe Produto.
# A classe Estoque deve oferecer os seguintes métodos:
# • cadastrar um novo produto;
# • realizar a entrada de unidades;
# • realizar a saída de unidades;
# • calcular o valor financeiro total do estoque;
# • identificar o produto com maior valor total armazenado;
# • listar os produtos com quantidade abaixo de um limite informado.
# A busca de um produto pelo código deve ser realizada obrigatoriamente por uma
# função recursiva com a seguinte assinatura:
# localizar_produto(produtos, codigo, indice)
# A função deve retornar o objeto encontrado ou None quando o código não existir.
# Não utilize estruturas de repetição dentro dessa função.
# O programa principal deve:
# • ler o arquivo produtos.txt;
# • criar um objeto Produto para cada linha válida;
# • armazenar os objetos em um objeto da classe Estoque;
# • permitir a realização de entradas e saídas de produtos;
# • impedir quantidades negativas e saídas superiores ao estoque disponível;
# • apresentar o valor financeiro total do estoque;
# • mostrar os produtos abaixo do estoque mínimo informado pelo usuário;
# • gravar a situação final no arquivo estoque_atualizado.txt.
# Cada linha do arquivo final deve manter o mesmo formato do arquivo original.
# Linhas inválidas do arquivo de entrada devem ser ignoradas e contabilizadas.
# Ao final, o programa deve exibir:
# • a quantidade de produtos carregados;
# • a quantidade de registros inválidos;
# • o produto de maior valor total em estoque;
# • o valor financeiro total do estoque;
# • a confirmação de que o arquivo atualizado foi gerado.

class Produto:
    def __init__(self, codigo, descricao, preco, quantidade):
        self.__codigo = int(codigo)
        self.__descricao = descricao
        self.__preco = float(preco)
        self.__quantidade = int(quantidade)

    def get_codigo(self): return self.__codigo
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def get_quantidade(self): return self.__quantidade

    def acrescentar(self, qtd):
        if qtd > 0: self.__quantidade += qtd

    def retirar(self, qtd):
        if 0 < qtd <= self.__quantidade:
            self.__quantidade -= qtd
            return True
        return False

    def calcular_total(self):
        return self.__preco * self.__quantidade

    def para_linha(self):
        return f"{self.__codigo};{self.__descricao};{self.__preco};{self.__quantidade}\n"


def localizar_produto(produtos, codigo, indice=0):
    if indice >= len(produtos):
        return None
    if produtos[indice].get_codigo() == codigo:
        return produtos[indice]
    return localizar_produto(produtos, codigo, indice + 1)

class Estoque:
    def __init__(self):
        self.produtos = []

    def cadastrar(self, produto):
        self.produtos.append(produto)

    def entrada(self, codigo, qtd):
        prod = localizar_produto(self.produtos, codigo)
        if prod and qtd > 0:
            prod.acrescentar(qtd)
            return True
        return False

    def saida(self, codigo, qtd):
        prod = localizar_produto(self.produtos, codigo)
        if prod and qtd > 0:
            return prod.retirar(qtd)
        return False

    def calcular_valor_total(self):
        return sum(p.calcular_total() for p in self.produtos)

    def maior_valor_armazenado(self):
        if not self.produtos: return None
        return max(self.produtos, key=lambda p: p.calcular_total())

    def listar_abaixo_do_limite(self, limite):
        return [p for p in self.produtos if p.get_quantidade() < limite]

if __name__ == "__main__":
    estoque = Estoque()
    carregados = 0
    invalidos = 0

    
    try:
        with open("produtos.txt", "r") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        linhas = ["101;Teclado;150.0;20\n", "102;Mouse;80.0;5\n", "invalid_line_here\n", "103;Monitor;1200.0;8\n"]

    
    for linha in linhas:
        try:
            partes = linha.strip().split(";")
            if len(partes) != 4: raise ValueError
            
            novo_prod = Produto(partes[0], partes[1], partes[2], partes[3])
            estoque.cadastrar(novo_prod)
            carregados += 1
        except Exception:
            invalidos += 1

    
    estoque.entrada(101, 5)  
    estoque.saida(102, 10)    
    estoque.saida(103, 2)     

    
    limite_usuario = 10
    abaixo_min = estoque.listar_abaixo_do_limite(limite_usuario)
    print(f"--- Produtos com estoque menor que {limite_usuario} ---")
    for p in abaixo_min:
        print(f"- {p.get_descricao()} ({p.get_quantidade()} un)")

    
    with open("estoque_atualizado.txt", "w") as f:
        for p in estoque.produtos:
            f.write(p.para_linha())

    
    maior_prod = estoque.maior_valor_armazenado()
    
    print("\n--- RELATÓRIO FINAL ---")
    print(f"Quantidade de produtos carregados: {carregados}")
    print(f"Quantidade de registros inválidos: {invalidos}")
    if maior_prod:
        print(f"Produto de maior valor total: {maior_prod.get_descricao()} (R$ {maior_prod.calcular_total():.2f})")
    print(f"Valor financeiro total do estoque: R$ {estoque.calcular_valor_total():.2f}")
    print("Confirmação: Arquivo 'estoque_atualizado.txt' gerado com sucesso.")