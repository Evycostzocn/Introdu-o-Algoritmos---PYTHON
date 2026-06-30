# open("caminho", "r")

# Mode
# r - Leitura
# w - Escrita
# a - Append / Incrementar
# x - Criar arquivo
# r+ - Leitura + escrita

arquivo = open("PYTHON - ARQUIVOS/teste.txt", "a")

# # print(arquivo.readable())
# # print(arquivo.read())

# # print(arquivo.readline())

# lista = arquivo.readlines() # transforma em lista
# print(lista[3])

arquivo.write("SQL\n")
arquivo.write("C++")

arquivo.close()


