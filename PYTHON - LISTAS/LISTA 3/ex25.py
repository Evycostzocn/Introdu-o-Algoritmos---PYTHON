# 25. Crie uma classe chamada Aluno, contendo os atributos:
# • matrícula;
# • nome;
# • nota da primeira avaliação;
# • nota da segunda avaliação;
# • nota da terceira avaliação.
# As notas devem estar no intervalo de 0 a 100.
# Implemente os métodos:
# • alterar_nota(numero_avaliacao, nova_nota);
# • calcular_media();
# • obter_situacao();
# • exibir_boletim().
# O método obter_situacao() deve retornar:
# • "Aprovado", para média maior ou igual a 70;
# • "Exame Especial", para média maior ou igual a 40 e menor que 70;
# • "Reprovado", para média menor que 40.
# No programa principal, crie uma lista de objetos da classe Aluno e exiba:
# • o boletim de cada aluno;
# • o aluno com maior média;
# • a média geral da turma;
# 16
# • a quantidade de alunos em cada situação.

# --- CLASSE ALUNO ---
class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        # Valida se as notas iniciais estão no intervalo de 0 a 100
        self.nota1 = max(0, min(100, nota1))
        self.nota2 = max(0, min(100, nota2))
        self.nota3 = max(0, min(100, nota3))

    def alterar_nota(self, numero_avaliacao, nova_nota):
        if 0 <= nova_nota <= 100:
            if numero_avaliacao == 1: self.nota1 = nova_nota
            elif numero_avaliacao == 2: self.nota2 = nova_nota
            elif numero_avaliacao == 3: self.nota3 = nova_nota

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def obter_situacao(self):
        media = self.calcular_media()
        if media >= 70:
            return "Aprovado"
        elif media >= 40:
            return "Exame Especial"
        else:
            return "Reprovado"

    def exibir_boletim(self):
        print(f"Matrícula: {self.matricula} | Nome: {self.nome}")
        print(f"Notas: [{self.nota1:.1f}, {self.nota2:.1f}, {self.nota3:.1f}]")
        print(f"Média: {self.calcular_media():.1f} | Situação: {self.obter_situacao()}\n")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Criando uma lista de alunos
    turma = [
        Aluno(202601, "Alice", 85, 90, 75),
        Aluno(202602, "Bob", 50, 60, 55),
        Aluno(202603, "Charlie", 30, 45, 25),
        Aluno(202604, "David", 95, 85, 100),
        Aluno(202605, "Eva", 40, 40, 40)
    ]

    # Alterando uma nota para testar o método
    turma[1].alterar_nota(1, 65)  # Altera a nota 1 do Bob de 50 para 65

    # 1. Exibir o boletim de cada aluno
    print("--- BOLETIM DOS ALUNOS ---")
    for aluno in turma:
        aluno.exibir_boletim()

    # Variáveis para estatísticas
    maior_media_aluno = turma[0]
    soma_medias = 0
    contagem_situacoes = {"Aprovado": 0, "Exame Especial": 0, "Reprovado": 0}

    # Processando os dados da lista
    for aluno in turma:
        media_atual = aluno.calcular_media()
        soma_medias += media_atual
        
        # Identificar maior média
        if media_atual > maior_media_aluno.calcular_media():
            maior_media_aluno = aluno
            
        # Contabilizar situações
        situacao = aluno.obter_situacao()
        contagem_situacoes[situacao] += 1

    media_geral = soma_medias / len(turma)

    # Exibindo os resultados das estatísticas
    print("--- ESTATÍSTICAS DA TURMA ---")
    print(f"Aluno com maior média: {maior_media_aluno.nome} ({maior_media_aluno.calcular_media():.1f})")
    print(f"Média geral da turma: {media_geral:.1f}")
    print("\nQuantidade de alunos por situação:")
    for sit, qtd in contagem_situacoes.items():
        print(f"- {sit}: {qtd}")