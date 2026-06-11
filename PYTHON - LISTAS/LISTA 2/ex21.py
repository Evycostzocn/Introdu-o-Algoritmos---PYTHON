"""
21. O sistema de uma universidade controla o acesso dos alunos a um laboratório especial. Para entrar no laboratório, cada aluno deve atender a algumas regras relacionadas à idade, 
ao treinamento obrigatório e à autorização do responsável.
Crie uma função chamada acesso_liberado(idade, treinamento, autorizacao)
que receba:
• idade: idade do aluno;
• treinamento: valor booleano indicando se o aluno realizou o treinamento
obrigatório;
• autorizacao: valor booleano indicando se o aluno possui autorização do
responsável.
A função deve retornar a string "Permitido" ou "Negado", de acordo com as
seguintes regras:
• alunos com 18 anos ou mais podem entrar apenas se tiverem realizado o treinamento obrigatório;
• alunos menores de 18 anos podem entrar apenas se tiverem realizado o treinamento obrigatório e possuírem autorização do responsável;
• alunos sem treinamento obrigatório nunca podem entrar, independentemente
da idade ou da autorização.
Depois, crie um programa principal que leia os dados de vários alunos. Para cada
aluno, devem ser lidas as seguintes informações:
• nome do aluno;
• idade;
• se realizou o treinamento obrigatório;
• se possui autorização do responsável.
A leitura deve continuar até que seja informada a idade 0. Quando isso acontecer,
o programa deve encerrar a leitura e não deve cadastrar esse aluno.
Para cada aluno lido, o programa deve utilizar a função acesso_liberado para
verificar se o acesso será permitido ou negado.
Ao final, o programa deve criar um dicionário chamado relatorio_acessos, no
seguinte formato:
{
"Permitido": ["Ana", "Carlos"],
"Negado": ["Bruno", "Marina"]
}
Nesse dicionário:
• a chave "Permitido" deve armazenar uma lista com os nomes dos alunos
que tiveram acesso liberado;
• a chave "Negado" deve armazenar uma lista com os nomes dos alunos que
tiveram acesso negado.
Além disso, ao final, o programa deve exibir:
• o dicionário relatorio_acessos;
• a quantidade total de alunos com acesso permitido;
• a quantidade total de alunos com acesso negado;
• uma mensagem indicando se a maioria dos alunos teve acesso permitido, acesso
negado ou se houve empate.
"""

def acesso_liberado(idade, treinamento, autorizacao):
    if idade >= 18 and treinamento:
        return True
    elif idade < 18 and treinamento and autorizacao:
        return True
    else:
        return False
    
def main():
    relatorio_acessos = {
        "Permitido": [],
        "Negado": []
    }
    while True:
        idade = int(input("Idade do aluno: "))
        if idade == 0:
            print("Programa encerrado")
            break
        nome = input("Digite o nome do aluno: ")
        treinamento = input("Possui treinamento (s/n): ")
        treinamento = treinamento.lower()
        autorizacao = input("Possui autorização (s/n): ")
        autorizacao = autorizacao.lower()

        if treinamento == "s":
            treinamento = True
        else:
            treinamento = False
        if autorizacao == "s":
            autorizacao = True
        else:
            autorizacao = False
        
        acesso = acesso_liberado(idade, treinamento, autorizacao)

        if acesso:
            relatorio_acessos["Permitido"].append(nome)
        else:
            relatorio_acessos["Negado"].append(nome)

    print(f"Alunos permitidos: {relatorio_acessos['Permitido']}")
    print(f"Alunos negados: {relatorio_acessos['Negado']}")

    permitidos = len(relatorio_acessos["Permitido"])
    negados = len(relatorio_acessos["Negado"])

    print(f"Quantidade permitidos: {permitidos}")
    print(f"Quantidade negados: {negados}")

    if permitidos > negados:
        print("-----------------------------")
        print("Maioria teve acesso permitido") 
        print("-----------------------------")
    elif negados > permitidos:
        print("-----------------------------")
        print("Maioria teve acesso negado") 
        print("-----------------------------")
    else:
        print("------")
        print("Empate") 
        print("------")
main()