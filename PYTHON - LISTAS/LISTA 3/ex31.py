# # 31. Uma universidade deseja informatizar parte de seu processo de matrícula. Considere
# # a descrição:
# # Cada aluno possui matrícula, nome e curso. Cada disciplina possui código, nome e carga horária. A oferta de uma disciplina em determinado
# # semestre é representada por uma turma. A turma possui número, semestre, professor, limite de vagas e uma lista de alunos matriculados.
# # Um aluno pode se matricular em várias turmas, e uma turma pode possuir
# # vários alunos. Entretanto, o aluno não pode se matricular duas vezes na
# # mesma turma. Uma matrícula somente pode ser realizada quando houver
# # vagas disponíveis.
# # A turma deve permitir a matrícula e o cancelamento da matrícula de
# # um aluno. O sistema também deve consultar as turmas de um aluno,
# # informar a quantidade de vagas restantes de uma turma e gerar uma lista
# # de chamada.
# # Realize a modelagem orientada a objetos do sistema.
# # Inicialmente, responda:
# # 20
# # a) Quais substantivos do texto representam possíveis classes?
# # b) Quais substantivos representam apenas atributos de outras classes?
# # c) Quais ações do texto representam possíveis métodos?
# # d) Qual é a diferença entre uma Disciplina e uma Turma?
# # e) Em qual classe deve ficar o método de matricular um aluno?
# # f) Como deve ser representada a relação entre alunos e turmas?
# # g) Qual objeto deve verificar se ainda existem vagas?
# # Em seguida, defina as classes com seus atributos, construtores e métodos.
# # No programa principal:
# # • crie diferentes disciplinas;
# # • crie pelo menos duas turmas;
# # • crie diferentes alunos;
# # • realize matrículas e cancelamentos;
# # • tente repetir uma matrícula;
# # • tente matricular um aluno em uma turma cheia;
# # • exiba a lista de chamada de cada turma;
# # • exiba as turmas em que cada aluno está matriculado.

# a) Substantivos que representam possíveis classes:

# Aluno, Disciplina e Turma.

# b) Substantivos que representam apenas atributos:

# matricula, nome (do aluno/disciplina/professor), curso, codigo, carga horaria, numero (da turma), semestre e limite de vagas.

# c) Ações que representam possíveis métodos:

# matricular_aluno(), cancelar_matricula(), consultar_turmas(), vagas_restantes() e gerar_lista_chamada().

# d) Diferença entre Disciplina e Turma:

# A Disciplina é a entidade abstrata/conceitual do catálogo da universidade (ex: Cálculo I, 60h). A Turma é a aplicação prática e concreta daquela disciplina em um espaço de tempo específico, com um professor, horário e limite de alunos (ex: Turma 01 de Cálculo I, no 1º Semestre de 2026, com o Professor Carlos).

# e) Em qual classe deve ficar o método de matricular um aluno?

# Na classe Turma, pois ela é quem detém a lista de alunos matriculados e o controle do limite de vagas daquela oferta.

# f) Como deve ser representada a relação entre alunos e turmas?

# Como uma relação de Muitos para Muitos (Associação). A Turma armazena uma lista de objetos Aluno e, para o sistema rastrear o inverso, o Aluno também pode guardar uma lista das Turmas em que se matriculou (ou o sistema faz essa varredura).

# g) Qual objeto deve verificar se ainda existem vagas?

# O objeto da classe Turma, pois ela possui o atributo limite_vagas e sabe quantos alunos já estão em sua lista.

# --- CLASSE ALUNO ---
class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.turmas = []  # Lista de turmas onde o aluno está matriculado

    def entrar_na_turma(self, turma):
        if turma not in self.turmas:
            self.turmas.append(turma)

    def sair_da_turma(self, turma):
        if turma in self.turmas:
            self.turmas.remove(turma)


# --- CLASSE DISCIPLINA ---
class Disciplina:
    def __init__(self, codigo, nome, carga_horaria):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria


# --- CLASSE TURMA ---
class Turma:
    def __init__(self, numero, semestre, professor, limite_vagas, disciplina):
        self.numero = numero
        self.semestre = semestre
        self.professor = professor
        self.limite_vagas = limite_vagas
        self.disciplina = disciplina  # Objeto Disciplina associado
        self.alunos_matriculados = []

    def vagas_restantes(self):
        return self.limite_vagas - len(self.alunos_matriculados)

    def matricular_aluno(self, aluno):
        # 1. Verificar se o aluno já está matriculado nesta turma
        if aluno in self.alunos_matriculados:
            print(f"Erro: O aluno {aluno.nome} já está matriculado na Turma {self.numero} ({self.disciplina.nome}).")
            return False

        # 2. Verificar se há vagas disponíveis
        if self.vagas_restantes() <= 0:
            print(f"Erro: Não há vagas disponíveis na Turma {self.numero} ({self.disciplina.nome}).")
            return False

        # 3. Efetivar matrícula (Vínculo bidirecional)
        self.alunos_matriculados.append(aluno)
        aluno.entrar_na_turma(self)
        print(f"Sucesso: {aluno.nome} matriculado na Turma {self.numero} de {self.disciplina.nome}.")
        return True

    def cancelar_matricula(self, aluno):
        if aluno in self.alunos_matriculados:
            self.alunos_matriculados.remove(aluno)
            aluno.sair_da_turma(self)
            print(f"Cancelamento: Matrícula de {aluno.nome} cancelada na Turma {self.numero}.")
            return True
        print(f"Erro: Aluno {aluno.nome} não encontrado nesta turma.")
        return False

    def gerar_lista_chamada(self):
        print(f"\n--- LISTA DE CHAMADA - TURMA {self.numero} ({self.disciplina.nome}) ---")
        print(f"Professor: {self.professor} | Semestre: {self.semestre}")
        print(f"Vagas Restantes: {self.vagas_restantes()}")
        print("-" * 50)
        if not self.alunos_matriculados:
            print("Nenhum aluno matriculado.")
        for i, aluno in enumerate(self.alunos_matriculados, 1):
            print(f"{i:02d}. [Matrícula: {aluno.matricula}] {aluno.nome} ({aluno.curso})")
        print("-" * 50)


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # 1. Criar disciplinas
    d1 = Disciplina("COMP-01", "Programação Orientada a Objetos", 60)
    d2 = Disciplina("MATH-02", "Cálculo Diferencial e Integral", 80)

    # 2. Criar duas turmas (Turma 101 com apenas 2 vagas para testar o limite)
    t1 = Turma(101, "2026/1", "Prof. Alfredo", 2, d1)
    t2 = Turma(202, "2026/1", "Prof. Ricardo", 40, d2)

    # 3. Criar alunos
    a1 = Aluno(1001, "Ana Beatriz", "Ciência da Computação")
    a2 = Aluno(1002, "Carlos Eduardo", "Engenharia de Software")
    a3 = Aluno(1003, "Daniela Rocha", "Sistemas de Informação")

    print("--- REALIZANDO MATRÍCULAS ---")
    t1.matricular_aluno(a1)
    t1.matricular_aluno(a2)
    
    t2.matricular_aluno(a1)
    t2.matricular_aluno(a3)

    print("\n--- TESTANDO RESTRIÇÕES ---")
    # Tentar repetir matrícula
    t1.matricular_aluno(a1)
    
    # Tentar matricular em turma cheia (t1 só tinha 2 vagas, preenchidas por a1 e a2)
    t1.matricular_aluno(a3)

    print("\n--- TESTANDO CANCELAMENTO ---")
    t1.cancelar_matricula(a2)  # Libera uma vaga na t1
    t1.matricular_aluno(a3)    # Agora a Daniela consegue entrar

    print("\n--- EXIBINDO LISTAS DE CHAMADA ---")
    t1.gerar_lista_chamada()
    t2.gerar_lista_chamada()

    print("\n--- CONSULTANDO TURMAS POR ALUNO ---")
    for aluno in [a1, a2, a3]:
        print(f"Aluno: {aluno.nome} está matriculado em:")
        if not aluno.turmes:
            print("  Nenhuma turma.")
        for t in aluno.turmas:
            print(f"  - Turma {t.numero}: {t.disciplina.nome}")