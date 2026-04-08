palavra = input("Digite uma palavra: ")
eh_palindromo = True
for i in range(len(palavra)):
    if palavra[i] != palavra[len(palavra) - 1 - i]:
        eh_palindromo = False
        break
print(eh_palindromo)