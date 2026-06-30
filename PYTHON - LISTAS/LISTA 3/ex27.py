# # 27. Leia a descrição a seguir:
# # Uma clínica veterinária atende animais pertencentes a diferentes clientes.
# # Para cada cliente, são registrados nome, CPF e telefone. Cada animal
# # possui nome, espécie, raça, data de nascimento e peso. Um cliente pode
# # possuir vários animais, mas cada animal pertence a apenas um cliente.
# # Durante uma consulta, o veterinário registra a data, o motivo do atendimento, o diagnóstico e o valor cobrado. Um animal pode passar por
# # várias consultas. O sistema deve permitir cadastrar clientes e animais,
# # alterar o peso de um animal, registrar uma consulta, consultar o histórico
# # de atendimentos de um animal e calcular o valor total gasto pelo cliente.
# # 17
# # Antes de implementar, faça a modelagem do sistema:
# # a) Identifique as classes necessárias.
# # b) Liste os atributos de cada classe.
# # c) Liste os métodos que devem pertencer a cada classe.
# # d) Indique os relacionamentos existentes entre as classes.
# # e) Informe quais objetos devem armazenar listas de outros objetos.
# # Em seguida, implemente as classes propostas e crie um programa principal que:
# # • cadastre pelo menos dois clientes;
# # • cadastre animais para esses clientes;
# # • registre diferentes consultas;
# # • exiba o histórico de um animal;
# # • calcule o total gasto por cada cliente.
# # Evite criar uma única classe responsável por todas as operações. Cada comportamento deve ser colocado na classe que possui os dados necessários para realizá-lo.

# a) Classes Necessárias:

# Cliente, Animal e Consulta.

# b) Atributos:

# Cliente: nome, cpf, telefone, animais (lista).

# Animal: nome, especie, raca, data_nascimento, peso, consultas (lista).

# Consulta: data, motivo, diagnostico, valor.

# c) Métodos:

# Cliente: adicionar_animal(animal), calcular_total_gasto().

# Animal: alterar_peso(novo_peso), registrar_consulta(consulta), exibir_historico().

# Consulta: exibir_detalhes().

# d) Relacionamentos:

# Um Cliente possui uma lista de Animais (Composição/Associação 1 para Muitos).

# Um Animal possui uma lista de Consultas (Composição/Associação 1 para Muitos).

# e) Listas de outros objetos:

# O objeto Cliente armazena uma lista de objetos Animal.

# O objeto Animal armazena uma lista de objetos Consulta.

# --- CLASSE CONSULTA ---
class Consulta:
    def __init__(self, data, motivo, diagnostico, valor):
        self.data = data
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.valor = float(valor)

    def exibir_detalhes(self):
        print(f"  Data: {self.data} | Motivo: {self.motivo} | Diagnóstico: {self.diagnostico} | Valor: R$ {self.valor:.2f}")


# --- CLASSE ANIMAL ---
class Animal:
    def __init__(self, nome, especie, raca, data_nascimento, peso):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.data_nascimento = data_nascimento
        self.peso = float(peso)
        self.consultas = []  # Lista de objetos Consulta

    def alterar_peso(self, novo_peso):
        if novo_peso > 0:
            self.peso = novo_peso

    def registrar_consulta(self, consulta):
        self.consultas.append(consulta)

    def calcular_total_consultas(self):
        return sum(c.valor for c in self.consultas)

    def exibir_historico(self):
        print(f"Histórico de {self.nome} ({self.especie} - {self.raca}, {self.peso}kg):")
        if not self.consultas:
            print("  Nenhuma consulta registrada.")
        for c in self.consultas:
            c.exibir_detalhes()
        print()


# --- CLASSE CLIENTE ---
class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.animais = []  # Lista de objetos Animal

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def calcular_total_gasto(self):
        return sum(a.calcular_total_consultas() for a in self.animais)


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # 1. Cadastrar Clientes
    c1 = Cliente("Carlos Roberto", "111.222.333-44", "(31) 99999-1111")
    c2 = Cliente("Mariana Souza", "555.666.777-88", "(31) 98888-2222")

    # 2. Cadastrar Animais para os clientes
    a1 = Animal("Rex", "Cão", "Vira-lata", "10/05/2022", 15.2)
    a2 = Animal("Mingau", "Gato", "Persa", "22/11/2023", 4.1)
    c1.adicionar_animal(a1)
    c1.adicionar_animal(a2)

    a3 = Animal("Thor", "Cão", "Pitbull", "01/02/2021", 32.0)
    c2.adicionar_animal(a3)

    # Alterar peso de um animal
    a1.alterar_peso(16.0)

    # 3. Registrar Consultas
    a1.registrar_consulta(Consulta("15/06/2026", "Vacina anual", "Saudável", 120.0))
    a1.registrar_consulta(Consulta("28/06/2026", "Dor na pata", "Torção leve", 180.0))
    
    a3.registrar_consulta(Consulta("30/06/2026", "Check-up", "Ótimo estado", 150.0))

    # 4. Exibir o histórico de um animal
    print("--- CONSULTA DE HISTÓRICO ---")
    a1.exibir_historico()

    # 5. Calcular o total gasto por cada cliente
    print("--- FATURAMENTO POR CLIENTE ---")
    print(f"Cliente: {c1.nome} | Total Gasto: R$ {c1.calcular_total_gasto():.2f}")
    print(f"Cliente: {c2.nome} | Total Gasto: R$ {c2.calcular_total_gasto():.2f}")