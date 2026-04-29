"""
Considere o código a seguir:
x = 0
y = 10
if x != 0 and y / x > 1:
    print("A")
else:
    print("B")
Determine se ocorre erro em tempo de execução, qual é a saída do programa e
explique o papel da avaliação de curto-circuito.
"""
x = 0
y = 10
if x != 0 and y / x > 1:
    print("A")
else:
    print("B")