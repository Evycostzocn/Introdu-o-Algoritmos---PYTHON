# # 28. Leia a descrição de um sistema de empréstimos de biblioteca:
# # A biblioteca mantém um catálogo de livros. Cada livro possui ISBN,
# # título, autor e quantidade de exemplares disponíveis. Os usuários da
# # biblioteca possuem matrícula, nome e uma lista de empréstimos.
# # Quando um usuário solicita um livro, o sistema deve verificar se existe
# # um exemplar disponível. Caso exista, um empréstimo é criado contendo
# # o livro, o usuário, a data do empréstimo, a data prevista para devolução
# # e a situação. Quando o livro é devolvido, a situação do empréstimo deve
# # ser alterada e a quantidade disponível deve ser atualizada.
# # Um usuário não pode manter mais de três empréstimos ativos. O sistema
# # também deve permitir consultar os empréstimos ativos de um usuário e
# # verificar quais livros estão indisponíveis.
# # Com base no texto:
# # a) Identifique pelo menos três classes necessárias.
# # b) Determine os atributos de cada classe.
# # c) Defina em qual classe deve ficar a responsabilidade de verificar a disponibilidade
# # de um livro.
# # d) Defina em qual classe deve ficar a responsabilidade de verificar o limite de
# # empréstimos do usuário.
# # 18
# # e) Explique por que a data prevista para devolução não deve ser um atributo da
# # classe Livro.
# # f) Represente os relacionamentos entre as classes.
# # Depois, implemente a modelagem e crie um programa principal que realize empréstimos, devoluções e consultas.

# Aqui está a resposta conceitual e a implementação do exercício 28 em Python:

# MODELAGEM DO SISTEMA
# a) Classes Necessárias:

# Livro, Usuario e Emprestimo.

# b) Atributos de cada classe:

# Livro: isbn, titulo, autor, qtd_disponivel.

# Usuario: matricula, nome, emprestimos (lista de objetos Emprestimo).

# Emprestimo: livro, usuario, data_emprestimo, data_devolucao_prevista, situacao (ex: "Ativo" ou "Devolvido").

# c) Responsabilidade de verificar a disponibilidade do livro:

# Deve ficar na classe Livro (ou em uma classe controladora/sistema que gerencie o acervo), pois ela possui o controle direto do atributo qtd_disponivel.

# d) Responsabilidade de verificar o limite de empréstimos do usuário:

# Deve ficar na classe Usuario, pois ela gerencia sua própria lista interna de empréstimos e consegue contar quantos deles estão com a situação "Ativo".

# e) Por que a data prevista para devolução não deve ser um atributo de Livro?

# Porque a data de devolução pertence ao contexto do vínculo temporário entre um usuário específico e o exemplar (ou seja, ao Emprestimo). Se ficasse na classe Livro, não seria possível gerenciar datas diferentes caso múltiplos usuários pegassem exemplares do mesmo livro simultaneamente.

# f) Relacionamentos:

# Um Usuario possui uma lista de Emprestimos (1 para Muitos).

# Um Emprestimo aponta para um Usuario e para um Livro específico (Associação).

from datetime import datetime, timedelta

# --- CLASSE LIVRO ---
class Livro:
    def __init__(self, isbn, titulo, autor, qtd_disponivel):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.qtd_disponivel = qtd_disponivel

    def esta_disponivel(self):
        return self.qtd_disponivel > 0

    def emprestar_exemplar(self):
        if self.esta_disponivel():
            self.qtd_disponivel -= 1
            return True
        return False

    def devolver_exemplar(self):
        self.qtd_disponivel += 1


# --- CLASSE EMPRÉSTIMO ---
class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now().strftime("%d/%m/%Y")
        # Previsão padrão de 14 dias para devolução
        self.data_devolucao_prevista = (datetime.now() + timedelta(days=14)).strftime("%d/%m/%Y")
        self.situacao = "Ativo"

    def registrar_devolucao(self):
        self.situacao = "Devolvido"
        self.livro.devolver_exemplar()


# --- CLASSE USUÁRIO ---
class Usuario:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.emprestimos = []

    def obter_emprestimos_ativos(self):
        return [emp for emp in self.emprestimos if emp.situacao == "Ativo"]

    def pode_pegar_emprestimo(self):
        return len(self.obter_emprestimos_ativos()) < 3

    def solicitar_emprestimo(self, livro):
        if not self.pode_pegar_emprestimo():
            print(f"Erro: {self.nome} atingiu o limite máximo de 3 empréstimos ativos.")
            return False
        
        if not livro.esta_disponivel():
            print(f"Erro: O livro '{livro.titulo}' está indisponível no momento.")
            return False

        if livro.emprestar_exemplar():
            novo_emprestimo = Emprestimo(livro, self)
            self.emprestimos.append(novo_emprestimo)
            print(f"Sucesso: Empréstimo de '{livro.titulo}' realizado para {self.nome}.")
            return True
        return False


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Criando Livros
    l1 = Livro("978-1", "Clean Code", "Robert C. Martin", 2)
    l2 = Livro("978-2", "Design Patterns", "Gang of Four", 1)
    l3 = Livro("978-3", "Refactoring", "Martin Fowler", 0)  # Indisponível

    # Criando Usuários
    u1 = Usuario(202651, "Rodrigo Melo")
    u2 = Usuario(202652, "Beatriz Rocha")

    print("--- SIMULAÇÃO DE EMPRÉSTIMOS ---")
    u1.solicitar_emprestimo(l1)  # Sucesso (Sobram 1)
    u1.solicitar_emprestimo(l2)  # Sucesso (Sobram 0)
    u1.solicitar_emprestimo(l3)  # Erro: Indisponível

    print("\n--- TESTANDO LIMITE DE 3 LIVROS ---")
    # Forçando u1 a pegar mais livros para estourar o limite
    l4 = Livro("978-4", "Livro Extra 1", "Autor X", 5)
    l5 = Livro("978-5", "Livro Extra 2", "Autor Y", 5)
    u1.solicitar_emprestimo(l4)  # Sucesso (3º ativo)
    u1.solicitar_emprestimo(l5)  # Erro: Limite atingido

    print("\n--- CONSULTA ATIVOS ---")
    ativos = u1.obter_emprestimos_ativos()
    for emp in ativos:
        print(f"Livro: {emp.livro.titulo} | Previsão: {emp.data_devolucao_prevista}")

    print("\n--- SIMULAÇÃO DE DEVOLUÇÃO ---")
    ativos[0].registrar_devolucao()  # Devolveu "Clean Code"
    print(f"Exemplares disponíveis de '{l1.titulo}': {l1.qtd_disponivel}")
    
    # Agora ele deve conseguir pegar o livro que foi negado antes
    u1.solicitar_emprestimo(l5)