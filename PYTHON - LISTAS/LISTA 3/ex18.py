# 18. Implemente uma classe chamada ContaBancaria. Cada objeto deve possuir os
# seguintes atributos privados:
# • número da conta;
# • nome do titular;
# • saldo;
# • limite de crédito;
# • histórico de operações.
# O construtor deve receber o número da conta, o nome do titular e o limite de crédito.
# Toda conta deve ser criada com saldo inicial igual a zero e histórico vazio.
# Implemente os seguintes métodos:
# • depositar(valor): adiciona um valor positivo ao saldo;
# • sacar(valor): realiza o saque apenas quando o valor for positivo e não
# ultrapassar a soma do saldo com o limite;
# • transferir(destino, valor): retira o valor da conta atual e o deposita
# em outro objeto da classe ContaBancaria;
# • consultar_saldo(): retorna o saldo atual;
# • consultar_saldo_disponivel(): retorna a soma do saldo com o limite;
# • exibir_extrato(): apresenta todas as operações realizadas na conta.
# Cada operação válida deve ser registrada no histórico, indicando seu tipo e valor.
# Operações inválidas não devem alterar o saldo nem o histórico.
# No programa principal:
# • crie pelo menos três contas;
# • realize depósitos, saques e transferências entre elas;
# • tente executar pelo menos uma operação inválida;
# • exiba o extrato e o saldo final de cada conta;
# • identifique a conta com maior saldo disponível.
# Os atributos não devem ser acessados ou modificados diretamente fora da classe.
 

class ContaBancaria:
    def __init__(self, num_conta, nome, limite_cartao):
        self.__saldo = 0
        self.__historico = []
        self.__nome = nome
        self.__num_conta = num_conta
        self.__limite_cartao = limite_cartao

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.append(f"Depósito: R$ {valor}")

    def sacar(self, valor):
        if valor > 0 and valor <= (self.__saldo + self.__limite_cartao):
            self.__saldo -= valor
            self.__historico.append(f"Valor sacado: R$ {valor}")
            print("Valor sacado!")
            return True
        else:
            print("Não foi possível realizar o saque!")
            return False

    def transferir(self, destino, valor):

        if self.sacar(valor):
            destino.depositar(valor)
            self.__historico.append(f"Transferência enviada: R$ {valor}")
    
    def consultar_saldo(self):
        return self.__saldo
    
    def consultar_saldo_disponivel(self):
        return self.__saldo + self.__limite_cartao
    
    def exibir_extrato(self):
        for operacao in self.__historico:
            print(operacao)

conta1 = ContaBancaria(1, "Evelyn", 500)
conta2 = ContaBancaria(2, "Gabriel", 300)
conta3 = ContaBancaria(3, "Maria", 1000)

conta1.depositar(1000)
conta2.depositar(500)
conta3.depositar(200)

conta1.sacar(300)
conta2.sacar(100)

conta1.transferir(conta2, 200)
conta3.transferir(conta1, 150)

conta2.sacar(5000)

print("\n===== CONTA 1 =====")
conta1.exibir_extrato()
print("Saldo:", conta1.consultar_saldo())
print("Saldo disponível:", conta1.consultar_saldo_disponivel())

print("\n===== CONTA 2 =====")
conta2.exibir_extrato()
print("Saldo:", conta2.consultar_saldo())
print("Saldo disponível:", conta2.consultar_saldo_disponivel())

print("\n===== CONTA 3 =====")
conta3.exibir_extrato()
print("Saldo:", conta3.consultar_saldo())
print("Saldo disponível:", conta3.consultar_saldo_disponivel())

maior = conta1

if conta2.consultar_saldo_disponivel() > maior.consultar_saldo_disponivel():
    maior = conta2

if conta3.consultar_saldo_disponivel() > maior.consultar_saldo_disponivel():
    maior = conta3

print("\nConta com maior saldo disponível:")
print(maior.consultar_saldo_disponivel())