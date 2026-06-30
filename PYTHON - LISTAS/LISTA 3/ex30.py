# 30. Analise os requisitos de um estacionamento:
# 19
# O estacionamento possui várias vagas numeradas. Cada vaga possui um
# tipo, que pode ser comum, para motocicleta ou para pessoa com deficiência, e pode estar livre ou ocupada.
# Cada veículo possui placa, modelo e tipo. Quando um veículo entra,
# deve ser direcionado a uma vaga compatível. O sistema registra o horário
# de entrada. Na saída, registra o horário de saída, calcula o tempo de
# permanência e determina o valor a pagar.
# O estacionamento deve informar a quantidade de vagas livres por tipo,
# localizar o veículo por sua placa, impedir que dois veículos ocupem a
# mesma vaga e impedir que o mesmo veículo seja registrado duas vezes.
# Antes da implementação:
# a) Identifique as possíveis classes do sistema.
# b) Diferencie as informações que pertencem ao veículo, à vaga e ao registro de
# permanência.
# c) Defina os métodos de cada classe.
# d) Indique qual classe deve localizar uma vaga disponível.
# e) Indique qual classe deve calcular o valor da permanência.
# f) Explique por que o horário de entrada não deve ser um atributo permanente
# da classe Veiculo.
# Implemente a solução e crie um programa principal que simule entradas e saídas,
# incluindo tentativas inválidas.

# a) Classes do Sistema
# Veiculo, Vaga, Ticket (ou RegistroPermanencia) e Estacionamento.

# b) Divisão das Informações
# Do Veículo: placa, modelo, tipo (comum, moto, pcd).

# Da Vaga: numero, tipo_compativel, ocupada.

# Do Registro (Ticket): veiculo, vaga, horario_entrada, horario_saida, ativo.

# c) Métodos de cada Classe
# Veiculo: Construtor e propriedades de acesso.

# Vaga: ocupar(), desocupar().

# Ticket: finalizar_registro(horario_saida), calcular_tempo(), calcular_valor().

# Estacionamento: registrar_entrada(veiculo, horario), registrar_saida(placa, horario), vagas_livres_por_tipo(), localizar_veiculo(placa).

# d) Localização de vaga disponível
# Cabe à classe Estacionamento, pois ela gerencia a coleção global de todas as vagas do pátio.

# e) Cálculo do valor da permanência
# Cabe à classe Ticket (ou RegistroPermanencia), pois ela possui os dados de tempo (entrada/saída) necessários para o cálculo financeiro.

# f) Por que o horário de entrada não pertence ao Veículo?
# O horário de entrada é um dado transacional e temporário. O veículo existe independentemente de estar ou não dentro do estacionamento. 
# Se colocássemos esse atributo na classe Veiculo,
# ele não conseguiria guardar o histórico de vezes anteriores que estacionou e violaria a separação de escopos.

# --- CLASSE VEÍCULO ---
class Veiculo:
    def __init__(self, placa, modelo, tipo):
        self.placa = placa
        self.modelo = modelo
        self.tipo = tipo  # "comum", "moto", "pcd"


# --- CLASSE VAGA ---
class Vaga:
    def __init__(self, numero, tipo_compativel):
        self.numero = numero
        self.tipo_compativel = tipo_compativel  # "comum", "moto", "pcd"
        self.ocupada = False

    def ocupar(self):
        self.ocupada = True

    def desocupar(self):
        self.ocupada = False


# --- CLASSE TICKET (REGISTRO) ---
class Ticket:
    def __init__(self, veiculo, vaga, horario_entrada):
        self.veiculo = veiculo
        self.vaga = vaga
        self.horario_entrada = horario_entrada  # Representado em minutos inteiros para simplificar
        self.horario_saida = None
        self.ativo = True

    def finalizar_registro(self, horario_saida):
        self.horario_saida = horario_saida
        self.ativo = False
        self.vaga.desocupar()

    def calcular_tempo(self):
        if self.horario_saida is not None:
            return self.horario_saida - self.horario_entrada
        return 0

    def calcular_valor(self):
        tempo = self.calcular_tempo()
        # Regra de negócio fictícia: R$ 0.20 por minuto (ou R$ 12,00 por hora)
        return tempo * 0.20


# --- CLASSE ESTACIONAMENTO ---
class Estacionamento:
    def __init__(self):
        self.vagas = []
        self.tickets = []

    def adicionar_vaga(self, vaga):
        self.vagas.append(vaga)

    def vagas_livres_por_tipo(self):
        contagem = {"comum": 0, "moto": 0, "pcd": 0}
        for v in self.vagas:
            if not v.ocupada:
                contagem[v.tipo_compativel] += 1
        return contagem

    def localizar_veiculo(self, placa):
        for t in self.tickets:
            if t.ativo and t.veiculo.placa == placa:
                return t.vaga.numero
        return None

    def registrar_entrada(self, veiculo, horario):
        # Impedir registro duplicado do mesmo veículo ativo
        if self.localizar_veiculo(veiculo.placa) is not None:
            print(f"Erro: Veículo com placa {veiculo.placa} já está dentro do estacionamento.")
            return False

        # Localizar vaga disponível e compatível
        vaga_encontrada = None
        for v in self.vagas:
            if not v.ocupada and v.tipo_compativel == veiculo.tipo:
                vaga_encontrada = v
                break

        if not vaga_encontrada:
            print(f"Erro: Não há vagas disponíveis para o tipo '{veiculo.tipo}'.")
            return False

        vaga_encontrada.ocupar()
        novo_ticket = Ticket(veiculo, vaga_encontrada, horario)
        self.tickets.append(novo_ticket)
        print(f"Sucesso: {veiculo.modelo} ({veiculo.placa}) estacionado na vaga {vaga_encontrada.numero}.")
        return True

    def registrar_saida(self, placa, horario_saida):
        ticket_ativo = None
        for t in self.tickets:
            if t.ativo and t.veiculo.placa == placa:
                ticket_ativo = t
                break

        if not ticket_ativo:
            print(f"Erro: Veículo com placa {placa} não foi localizado no pátio.")
            return

        ticket_ativo.finalizar_registro(horario_saida)
        print(f"Saída: {ticket_ativo.veiculo.modelo} liberado da vaga {ticket_ativo.vaga.numero}.")
        print(f"Tempo permanência: {ticket_ativo.calcular_tempo()} min | Valor a pagar: R$ {ticket_ativo.calcular_valor():.2f}")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    patio = Estacionamento()

    # Configurando o pátio com 4 vagas
    patio.adicionar_vaga(Vaga(1, "comum"))
    patio.adicionar_vaga(Vaga(2, "comum"))
    patio.adicionar_vaga(Vaga(3, "moto"))
    patio.adicionar_vaga(Vaga(4, "pcd"))

    # Criando veículos de teste
    carro1 = Veiculo("ABC-1234", "Civic", "comum")
    carro2 = Veiculo("XYZ-9999", "Corolla", "comum")
    moto1 = Veiculo("MOT-5555", "CG 160", "moto")
    carro_pcd = Veiculo("PCD-7777", "Spin", "pcd")

    print("--- SIMULAÇÃO DE ENTRADAS ---")
    patio.registrar_entrada(carro1, 60)       # Entra no minuto 60 (01:00h)
    patio.registrar_entrada(moto1, 70)        # Entra no minuto 70
    
    print("\n--- TESTANDO ENTRADAS INVÁLIDAS ---")
    patio.registrar_entrada(carro1, 80)       # Erro: Já cadastrado ativo
    
    # Lotando as vagas comuns
    patio.registrar_entrada(carro2, 85)       
    carro3 = Veiculo("KIP-4444", "Gol", "comum")
    patio.registrar_entrada(carro3, 90)       # Erro: Vagas comuns esgotadas

    print("\n--- CONSULTAS DE STATUS ---")
    print("Vagas livres por tipo:", patio.vagas_livres_por_tipo())
    print("Onde está o Civic?", patio.localizar_veiculo("ABC-1234"))

    print("\n--- SIMULAÇÃO DE SAÍDAS ---")
    patio.registrar_saida("ABC-1234", 120)    # Ficou 60 minutos (Deve dar R$ 12.00)
    patio.registrar_saida("OBL-0000", 200)    # Erro: Não existe no estacionamento