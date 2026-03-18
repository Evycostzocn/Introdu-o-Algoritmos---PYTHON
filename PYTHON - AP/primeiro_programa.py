x = 10.0
y = 3.14
z = "python"
w = True

# x = "dez" 

print(type(x))
print(type(y))
print(type(z))
print(type(w))


nome = "Evy"
idade = 19

print(f"\nHello, {nome}!")
print(f"você tem {idade} anos.")


valor = 1234.56789

print(f"\n{valor}")
print(f"{valor:.2f}")
print(f"{valor:.0f}")
print(f"{valor:.4f}")

nota1 = int(input("\nDigite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print(f"a média é: {media:.2f}")

c = int(input("digite a temperatura em celsius: "))

F = c * (9 / 5) + 32

print(F)


nome = input("digite o nome: ")
salario = float(input("digite o salario: "))
bonus = float(input("digite o percentual (valor entre 0 e 100): "))

valor_bonus = salario * (bonus / 100)

salario_final = salario + valor_bonus

print(f"o valor do bônus é {valor_bonus:.2f}")
print(f"o salario final é {salario_final:.2f}")



