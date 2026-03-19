"""Exercício 6 Controle de acesso ao laboratório
Um laboratório de informática possui regras específicas para acesso durante a noite.

O programa deve ler:

idade do usuário
se possui matrícula ativa (1 = sim, 0 = não)
se possui autorização especial (1 = sim, 0 = não)
Regras de acesso:

Estudantes com matrícula ativa e idade ≥ 18 podem entrar.
Estudantes com matrícula ativa menores de 18 só entram com autorização.
Pessoas sem matrícula ativa só entram com autorização.
O programa deve indicar:

Acesso permitido
ou
Acesso negado"""

idade = int(input("Idade: "))
matricula = bool(int(input("Matricula ativa (1 para sim e 0 para não): ")))
autorizacao = bool(int(input("Autorização especial: (1 para sim e 0 para não): ")))

if matricula == 1 and idade >= 18:
    print("Acesso permitido.")
elif matricula == 1 and idade < 18:
    if autorizacao == 1:
        print("Acesso permitido.")
    else:
        print("Acesso negado.")
elif matricula == 0 and idade > 18:
    if autorizacao == 1:
        print("Acesso permitido.")
    else: 
        print("Acesso negado.")
