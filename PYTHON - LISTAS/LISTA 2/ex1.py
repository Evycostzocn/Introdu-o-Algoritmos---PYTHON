"""
Você está desenvolvendo o módulo de segurança de um aplicativo financeiro. Durante o cadastro, o sistema pede ao usuário que crie uma senha. Crie uma função
validar_senha(senha) que verifique se a senha é segura. Uma senha é válida
se: tiver pelo menos 8 caracteres, contiver pelo menos um número, contiver pelo
menos uma letra maiúscula e não contiver espaços. O programa principal deve ler
senhas repetidamente até que o usuário digite "sair", imprimindo "Válida" ou "Inválida" para cada tentativa, e ao final informar a porcentagem de senhas válidas
testadas.
"""

def validar_senha(senha):

    temMaiuscula = False
    temNumero = False
    temEspaco = False

    for caracter in senha:
        if caracter.isdigit():
            temNumero = True
        if caracter.isupper():
            temMaiuscula = True
        if caracter == " ":
            temEspaco = True
    
    if len(senha) >= 8 and temNumero and temMaiuscula and not temEspaco:
        return True
    else:
        return False

validas = 0
invalidas = 0

while True:
    senha = input("Digite uma senha: ")
    if senha == "sair":
        break
    else: 
        resultado = validar_senha(senha)
        if resultado:
            print("VÁLIDA")
            validas += 1
        else:
            print("INVÁLIDA")
            invalidas += 1

total = validas + invalidas
if total > 0:
    porcentagemValidas = 100 * (validas / total)
    print(f"A PORCENTAGEM DE SENHAS VÁLIDAS É {porcentagemValidas:.1f}%")
    
    

