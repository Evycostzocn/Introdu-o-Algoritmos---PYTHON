"""
(Desafio) Você foi contratado para ajudar uma startup que está desenvolvendo um
novo aplicativo chamado SafeLogin, usado por estudantes para acessar materiais da
faculdade. Nos primeiros testes, a equipe percebeu que muitos usuários estavam
criando senhas muito fracas, o que representa um risco de segurança. Por isso,
pediram sua ajuda para criar uma verificação automática de senha. Durante o
cadastro, o sistema pede ao usuário que crie uma senha. Antes de aceitar, o sistema
precisa verificar se essa senha é segura o suficiente. Uma senha será considerada
válida apenas se atender às seguintes regras:
• Deve ter pelo menos 8 caracteres
• Deve conter pelo menos um número
• Deve conter pelo menos uma letra
Caso a senha não atenda a qualquer uma dessas regras, o sistema deve informar
que a senha é inválida. O seu código deve conter apenas estruturas condicionais, de
repetição, variáveis e operadores.
Dica: Pesquise por novas estratégias no python que possam te ajudar a resolver essa
questão."""

senha = input("Crie sua senha: ")
temLetra = False
temNumero = False

for caracter in len(senha):

    if caracter.isdigit():
        temNumero = True

    if caracter.isalpha():
        temLetra = True

if len(senha) >= 8 and temNumero and temLetra:
    print("Senha válida!")
else:
    print("senha inválida!")


