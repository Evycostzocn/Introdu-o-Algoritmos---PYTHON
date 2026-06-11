def contar_vogais(palavra, vogais):
    if len(palavra) == vogais:
        return 0
    elif "a" or "e" or "i" or "o" or "u" in palavra:
        return 1 + contar_vogais(palavra, vogais+1)
    else:
        return 0 + contar_vogais(palavra, vogais)
    
vogais = 0
palavra = input("digite uma palavra: ")
count = contar_vogais(palavra, vogais)
print(count)