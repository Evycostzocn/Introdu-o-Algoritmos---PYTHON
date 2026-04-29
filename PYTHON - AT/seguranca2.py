def criptografar(nome, senha):
    novoNome = ""
    novaSenha = ""
    novaCriptografia = ""
    for caracter in nome:
        novoNome += chr(ord(caracter) + 1)
    for caracter in senha:
        novaSenha += chr(ord(caracter) + 1)
    print(novoNome)
    print(novaSenha)
    novaCriptografia = novoNome + novaSenha
    print(novaCriptografia)

nome = input("nome: ")
senha = input("senha: ")

criptografar(nome, senha)