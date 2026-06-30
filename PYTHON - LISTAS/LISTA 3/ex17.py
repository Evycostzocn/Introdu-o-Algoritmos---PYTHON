# 17. Desenvolva uma função recursiva chamada
# eh_palindromo(texto, inicio, fim)
# que determine se um texto é um palíndromo. A função deve comparar os caracteres
# localizados nas posições inicio e fim e continuar a verificação em direção ao
# centro do texto.
# Durante a análise, a função deve:
# • desconsiderar diferenças entre letras maiúsculas e minúsculas;
# • ignorar espaços;
# • ignorar os caracteres de pontuação ., ,, :, ;, ! e ?;
# • retornar True quando o texto for um palíndromo e False caso contrário.
# Exemplos de textos que devem ser reconhecidos como palíndromos:
# "Socorram-me, subi no onibus em Marrocos"
# "Apos a sopa"
# "Anotaram a data da maratona"
# Não crie uma cópia invertida do texto e não utilize estruturas de repetição dentro
# da função recursiva.
# No programa principal, leia frases até que seja informada a palavra "fim". Ao
# final, exiba a quantidade de frases palíndromas e não palíndromas analisadas.

# --- FUNÇÃO RECURSIVA OBRIGATÓRIA ---
def eh_palindromo(texto, inicio, fim):
    # Caso Base 1: Se os índices se cruzarem ou se igualarem, chegamos ao centro
    if inicio >= fim:
        return True

    # Caracteres que devem ser ignorados
    ignorar = " .,;:!?- "

    # Se o caractere da esquerda for inválido, pula ele avançando o início
    if texto[inicio] in ignorar:
        return eh_palindromo(texto, inicio + 1, fim)

    # Se o caractere da direita for inválido, pula ele recuando o fim
    if texto[fim] in ignorar:
        return eh_palindromo(texto, inicio, fim - 1)

    # Compara os caracteres em minúsculo
    if texto[inicio].lower() == texto[fim].lower():
        # Avança em direção ao centro do texto
        return eh_palindromo(texto, inicio + 1, fim - 1)
    
    # Se forem diferentes, não é palíndromo
    return False


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    palindromas = 0
    nao_palindromas = 0

    while True:
        frase = input("Digite uma frase (ou 'fim' para sair): ").strip()
        
        if frase.lower() == "fim":
            break

        # Passa o índice inicial (0) e o índice final (tamanho da string - 1)
        if eh_palindromo(frase, 0, len(frase) - 1):
            print("-> É um palíndromo!")
            palindromas += 1
        else:
            print("-> Não é um palíndromo.")
            nao_palindromas += 1

    print("\n--- ANÁLISE FINAL ---")
    print(f"Frases palíndromas: {palindromas}")
    print(f"Frases não palíndromas: {nao_palindromas}")