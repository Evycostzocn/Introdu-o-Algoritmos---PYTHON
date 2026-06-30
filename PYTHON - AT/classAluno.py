class Aluno:
    def __init__(self,nome, matricula, nota1, nota2):
        
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")

    def alterar_nota(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

aluno1 = Aluno("João", 20, 8.0, 7.0)
aluno1.exibir_dados()
print("\n")
aluno1.alterar_nota(9.0, 10.0)
aluno1.exibir_dados()