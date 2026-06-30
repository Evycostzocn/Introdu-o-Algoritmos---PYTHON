# class Carro:
#     # O método __init__ é o construtor, chamado ao criar um novo objeto
#     def __init__(self, marca, modelo):
#         self.marca = marca   # Atributo do objeto
#         self.modelo = modelo # Atributo do objeto
#         self.ligado = False  # Estado inicial padrão

#     # Um método (comportamento)
#     def ligar(self):
#         self.ligado = True
#         print(f"O {self.marca} {self.modelo} está ligado.")

# # Criando (instanciando) um objeto
# meu_carro = Carro("Toyota", "Corolla")
# meu_carro.ligar()

class Item:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class Inventario:

    def __init__(self, itens = []):
        self.itens = []
    
    def adicionar_item(self, itens):
        self.itens.append(Item)

    def exibir_itens(self):
        print(self.itens)

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = Inventario()
    
    def coletar(self, item):
        self.inventario
