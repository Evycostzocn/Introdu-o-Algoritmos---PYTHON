# 26. Crie uma classe chamada Elevador. Antes de escrever o código, identifique quais
# informações devem representar o estado de um elevador.
# Considere que o elevador precisa controlar:
# • o andar atual;
# • a quantidade total de andares do prédio;
# • a capacidade máxima de pessoas;
# • a quantidade atual de pessoas;
# • se a porta está aberta ou fechada.
# O elevador deve ser criado no térreo, vazio e com a porta fechada.
# Defina e implemente métodos para permitir que o elevador:
# • abra e feche a porta;
# • receba a entrada de uma pessoa;
# • permita a saída de uma pessoa;
# • suba um andar;
# • desça um andar;
# • exiba seu estado atual.
# As seguintes regras devem ser respeitadas:
# • pessoas somente podem entrar ou sair com a porta aberta;
# • o elevador não pode ultrapassar sua capacidade;
# • o elevador não pode se movimentar com a porta aberta;
# • o elevador não pode subir além do último andar;
# • o elevador não pode descer abaixo do térreo.
# No programa principal, crie um objeto da classe e simule uma sequência de operações
# válidas e inválidas.

# --- CLASSE ELEVADOR ---
class Elevador:
    def __init__(self, total_andares, capacidade_maxima):
        self.andar_atual = 0  # 0 representa o térreo
        self.total_andares = total_andares
        self.capacidade_maxima = capacidade_maxima
        self.qtd_pessoas = 0
        self.porta_aberta = False

    def abrir_porta(self):
        self.porta_aberta = True
        print("Porta aberta.")

    def fechar_porta(self):
        self.porta_aberta = False
        print("Porta fechada.")

    def entrar_pessoa(self):
        if not self.porta_aberta:
            print("Erro: A porta está fechada. A pessoa não pode entrar.")
        elif self.qtd_pessoas >= self.capacidade_maxima:
            print("Erro: Elevador lotado. Capacidade máxima atingida.")
        else:
            self.qtd_pessoas += 1
            print("Uma pessoa entrou.")

    def sair_pessoa(self):
        if not self.porta_aberta:
            print("Erro: A porta está fechada. A pessoa não pode sair.")
        elif self.qtd_pessoas <= 0:
            print("Erro: O elevador já está vazio.")
        else:
            self.qtd_pessoas -= 1
            print("Uma pessoa saiu.")

    def subir(self):
        if self.porta_aberta:
            print("Erro: Não é seguro subir com a porta aberta!")
        elif self.andar_atual >= self.total_andares:
            print("Erro: O elevador já está no último andar.")
        else:
            self.andar_atual += 1
            print(f"Subiu para o {self.andar_atual}º andar.")

    def descer(self):
        if self.porta_aberta:
            print("Erro: Não é seguro descer com a porta aberta!")
        elif self.andar_atual <= 0:
            print("Erro: O elevador já está no térreo.")
        else:
            self.andar_atual -= 1
            print(f"Desceu para o {self.andar_atual if self.andar_atual > 0 else 'Térreo'}.")

    def exibir_estado(self):
        status_porta = "Aberta" if self.porta_aberta else "Fechada"
        andar_str = "Térreo" if self.andar_atual == 0 else f"{self.andar_atual}º andar"
        print(f"[Elevador] Andar: {andar_str} | Pessoas: {self.qtd_pessoas}/{self.capacidade_maxima} | Porta: {status_porta}")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Criando um elevador para um prédio de 5 andares e capacidade para 2 pessoas
    elevador = Elevador(total_andares=5, capacidade_maxima=2)
    
    print("--- ESTADO INICIAL ---")
    elevador.exibir_estado()

    print("\n--- TESTANDO OPERAÇÕES INVÁLIDAS ---")
    elevador.entrar_pessoa()  # Erro: Porta fechada
    elevador.subir()          # Funciona: Vai para o 1º andar
    elevador.abrir_porta()
    elevador.subir()          # Erro: Porta aberta

    print("\n--- TESTANDO CONTROLE DE CAPACIDADE ---")
    elevador.entrar_pessoa()  # Pessoa 1 entra
    elevador.entrar_pessoa()  # Pessoa 2 entra
    elevador.entrar_pessoa()  # Erro: Excede capacidade máxima (2)

    print("\n--- MOVIMENTAÇÃO VÁLIDA ---")
    elevador.fechar_porta()
    elevador.subir()          # Vai para o 2º andar
    elevador.subir()          # Vai para o 3º andar
    elevador.exibir_estado()

    print("\n--- TESTANDO LIMITES DOS ANDARES ---")
    elevador.subir()          # 4º andar
    elevador.subir()          # 5º andar (último)
    elevador.subir()          # Erro: Já está no último andar