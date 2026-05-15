"""
Exercício Integrador 1 Fechamento de pedido de uma cafeteria
Uma cafeteria deseja organizar melhor o fechamento dos pedidos. Para isso, o sistema deve calcular o valor do café, o valor do acompanhamento, 
gerar pequenos resumos dos itens e, ao final, calcular os totais do pedido.

Neste exercício, você deverá construir um pequeno projeto com dois arquivos Python:

funcoes_cafeteria.py, contendo as funções;
principal_cafeteria.py, contendo a lógica principal do programa.
Funções que devem ser implementadas no arquivo funcoes_cafeteria.py
1) calcular_preco_cafe(preco_base, acrescimo=0)

Crie uma função que receba o preço base de um café e um acréscimo opcional referente ao tamanho escolhido. A função deve retornar o preço final da bebida.

Exemplo:

Entrada: preco_base = 8.0, acrescimo = 2.0
Saída esperada: 10.0
2) calcular_acompanhamento(preco, desconto=0)

Crie uma função que receba o preço de um acompanhamento e um desconto percentual opcional. 
A função deve retornar o valor final do acompanhamento após aplicar o desconto informado.

Exemplo:

Entrada: preco = 12.0, desconto = 25
Saída esperada: 9.0
3) resumo_item(nome, valor)

Crie uma função que receba o nome de um item e seu valor final. A função deve retornar dois valores: uma string com a descrição do item e o valor formatado para exibição.

Exemplo:    

Entrada: nome = "Capuccino", valor = 10.5
Saída esperada: ("Capuccino", "R$ 10.50")
4) calcular_totais(valor1, valor2, taxa_servico=10)

Crie uma função que receba os valores de dois itens e uma taxa de serviço opcional. A função deve retornar três valores: subtotal, valor da taxa e total final do pedido.

Exemplo:

Entrada: valor1 = 10.0, valor2 = 8.0, taxa_servico = 10
Saída esperada: (18.0, 1.8, 19.8)
Lógica principal no arquivo principal_cafeteria.py
No arquivo principal, importe as funções criadas e desenvolva a lógica do sistema.

O programa deve:

ler o nome e o preço base do café;
ler o acréscimo opcional do tamanho;
ler o nome e o preço do acompanhamento;
ler o desconto opcional do acompanhamento;
calcular os valores finais dos dois itens;
gerar o resumo de cada item;
calcular subtotal, taxa e total do pedido;
exibir um resumo final do pedido.
Entradas sugeridas:

nome do café;
preço base do café;
acréscimo do tamanho;
nome do acompanhamento;
preço do acompanhamento;
desconto do acompanhamento;
taxa de serviço.
Saídas esperadas:

resumo do café;
resumo do acompanhamento;
subtotal;
taxa de serviço;
total final.
Observação: neste exercício, o objetivo é mostrar como funções com parâmetros opcionais e retornos múltiplos podem ser organizadas em um módulo separado 
e reutilizadas em um programa principal.
"""