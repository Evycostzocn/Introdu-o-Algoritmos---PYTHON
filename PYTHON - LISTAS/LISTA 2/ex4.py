"""
Um sistema de biblioteca utiliza um dicionário onde a chave é o ISBN do livro e o valor é uma lista [Titulo, Autor, Quantidade_Estoque]. Crie
funções para emprestar_livro(isbn) (reduz estoque ou avisa se não há) e
devolver_livro(isbn), que aumenta o estoque do livro devolvido.
"""
def emprestar_livro(isbn):
    if isbn in livros:
        if livros[isbn]["Quantidade_Estoque"] > 0:
            livros[isbn]["Quantidade_Estoque"] -= 1
            print("Empréstimo realizado")
        else:
            print("Não há livros para emprestar.")
    else:
        print("ISBN não encontrado.")

def devolver_livro(isbn):
    if isbn in livros:
        livros[isbn]["Quantidade_Estoque"] += 1
        print("Devolução realizada.")
    else:
        print("ISBN não foi encontrado")

livros = {

    "909090": {
        "Titulo": "Revolução dos Bichos", 
        "Autor": "George Orwell", 
        "Quantidade_Estoque": 5},
    "777777": {
        "Titulo": "Depois do Funeral", 
        "Autor": "Aghata Christie", 
        "Quantidade_Estoque": 12},
    "575733": {
        "Titulo": "Otelo", 
        "Autor": "Sheakespeare", 
        "Quantidade_Estoque": 2}
}

devolver_livro("909090")
print(livros)