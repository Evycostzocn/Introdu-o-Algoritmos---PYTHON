def criptografar():
    global novaPalavra
    palavra = input("palavra: ")
    novaPalavra = ""
    
    for caracter in palavra:
        
        novaPalavra += chr(ord(caracter) + 1)
    
criptografar()
print(novaPalavra)