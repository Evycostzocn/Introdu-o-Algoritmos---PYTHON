def separar_campos(linha):
    campos = []
    campo_atual = ""
    dentro_de_aspas = False
    i = 0

    while i < len(linha):
        c = linha[i]

        if c == '"':
        # se for aspas dupla escopada (""), vira uma aspas normal no texto.
            if dentro_de_aspas and i + 1 < len(linha) and linha[i + 1] == '"':
                campo_atual += '"'
                i += 1
            else:
                dentro_de_aspas = not dentro_de_aspas # invertendo o estado da variável dentro_de_aspas
        elif c == "," and not dentro_de_aspas:
            campos.append(campo_atual.strip()) # adicionando o campo atual ao array campos
            campo_atual = ""
        elif c != "\n" and c != "\n":
            campo_atual += c
        
        i += 1
    
    campos.append(campo_atual.strip())
    return campos

with open("data.csv", "r", encoding="utf-8") as data:
    next(data)
    for linha in data:
        info = separar_campos(linha)
        nome = info[14]
        ano = int(info[1])
        if (ano<1925):
            with open("musica_antiga.txt", "a", encoding="utf-8") as ma:
                ma.write(f"{nome}, {ano} \n")