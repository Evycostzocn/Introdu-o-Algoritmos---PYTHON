# 22. Crie uma classe chamada Livro para representar um livro que está sendo lido por
# uma pessoa.
# A classe deve possuir os seguintes atributos:
# • título;
# • autor;
# • quantidade total de páginas;
# • página atual da leitura.
# O construtor deve receber o título, o autor e a quantidade total de páginas. Todo
# objeto deve ser criado com a página atual igual a zero.
# Implemente os seguintes métodos:
# • avancar_paginas(quantidade): avança a leitura, sem permitir que a
# página atual ultrapasse o total de páginas;
# • voltar_paginas(quantidade): retorna páginas, sem permitir que a página atual fique negativa;
# • calcular_progresso(): retorna a porcentagem do livro que já foi lida;
# • finalizado(): retorna True quando todas as páginas tiverem sido lidas;
# • exibir_dados(): apresenta os dados do livro e o progresso da leitura.
# No programa principal, crie três objetos da classe Livro, realize diferentes operações de leitura e exiba os dados de cada objeto.

# --- CLASSE LIVRO ---
class Livro:
    def __init__(self, titulo, autor, total_paginas):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.pagina_atual = 0

    def avancar_paginas(self, quantidade):
        if quantidade > 0:
            if self.pagina_atual + quantidade <= self.total_paginas:
                self.pagina_atual += quantidade
            else:
                self.pagina_atual = self.total_paginas

    def voltar_paginas(self, quantidade):
        if quantidade > 0:
            if self.pagina_atual - quantidade >= 0:
                self.pagina_atual -= quantidade
            else:
                self.pagina_atual = 0

    def calcular_progresso(self):
        if self.total_paginas == 0:
            return 0.0
        return (self.pagina_atual / self.total_paginas) * 100

    def finalizado(self):
        return self.pagina_atual == self.total_paginas

    def exibir_dados(self):
        print(f"Título: {self.titulo} | Autor: {self.autor}")
        print(f"Páginas: {self.pagina_atual}/{self.total_paginas} ({self.calcular_progresso():.1f}% lido)")
        print(f"Status: {'Concluído' if self.finalizado() else 'Em leitura'}\n")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Criando os três livros
    livro1 = Livro("O Hobbit", "J.R.R. Tolkien", 300)
    livro2 = Livro("1984", "George Orwell", 320)
    livro3 = Livro("Duna", "Frank Herbert", 680)

    # Operações no Livro 1 (Avançar normal)
    livro1.avancar_paginas(150)
    
    # Operações no Livro 2 (Tentar passar do limite e depois voltar)
    livro2.avancar_paginas(400)  # Deve travar no total (320)
    livro2.voltar_paginas(50)

    # Operações no Livro 3 (Terminar o livro)
    livro3.avancar_paginas(680)

    # Exibindo os resultados
    print("--- STATUS DOS LIVROS ---")
    livro1.exibir_dados()
    livro2.exibir_dados()
    livro3.exibir_dados()