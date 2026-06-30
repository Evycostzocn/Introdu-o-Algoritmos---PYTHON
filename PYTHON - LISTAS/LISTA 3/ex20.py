# 20. Uma empresa possui diferentes categorias de funcionários. Implemente uma classebase chamada Funcionario, contendo os atributos privados ou protegidos:
# • matrícula;
# • nome;
# • salário-base.
# A classe deve possuir:
# • um construtor;
# • métodos de acesso aos atributos;
# • um método calcular_salario() que retorne o salário-base;
# • um método exibir_dados().
# Crie as seguintes classes derivadas:
# • Gerente, que possui uma gratificação fixa adicionada ao salário-base;
# • Vendedor, que possui um valor total de vendas e recebe uma comissão percentual sobre esse valor;
# • Desenvolvedor, que possui uma quantidade de horas extras e recebe um
# valor adicional por hora.
# Cada classe derivada deve sobrescrever o método calcular_salario() de acordo
# com sua regra.
# No programa principal:
# • crie uma única lista contendo objetos das diferentes classes;
# 12
# • percorra a lista e exiba os dados e o salário calculado de cada funcionário;
# • calcule o total da folha de pagamento;
# • identifique o funcionário com maior salário;
# • calcule a média salarial da empresa;
# • informe quantos funcionários recebem acima da média.
# O cálculo realizado no percurso da lista deve utilizar o mesmo método calcular_salario(),
# independentemente da classe concreta do objeto.


class Funcionario:
    def __init__(self, matricula, nome, salario_base):
        self._matricula = matricula 
        self._nome = nome
        self._salario_base = salario_base

    def get_nome(self):
        return self._nome

    def calcular_salario(self):
        return self._salario_base

    def exibir_dados(self):
        print(f"Matrícula: {self._matricula} | Nome: {self._nome}", end="")


class Gerente(Funcionario):
    def __init__(self, matricula, nome, salario_base, gratificacao):
        super().__init__(matricula, nome, salario_base)
        self._gratificacao = gratificacao

    def calcular_salario(self):
        return self._salario_base + self._gratificacao


class Vendedor(Funcionario):
    def __init__(self, matricula, nome, salario_base, total_vendas, percentual_comissao):
        super().__init__(matricula, nome, salario_base)
        self._total_vendas = total_vendas
        self._percentual_comissao = percentual_comissao

    def calcular_salario(self):
        return self._salario_base + (self._total_vendas * (self._percentual_comissao / 100))


class Desenvolvedor(Funcionario):
    def __init__(self, matricula, nome, salario_base, horas_extras, valor_hora_extra):
        super().__init__(matricula, nome, salario_base)
        self._horas_extras = horas_extras
        self._valor_hora_extra = valor_hora_extra

    def calcular_salario(self):
        return self._salario_base + (self._horas_extras * self._valor_hora_extra)


if __name__ == "__main__":
    funcionarios = [
        Gerente(101, "Ana Silva", 5000.0, 1500.0),
        Vendedor(102, "Bruno Costa", 2000.0, 50000.0, 5.0),
        Desenvolvedor(103, "Carlos Souza", 4000.0, 10, 50.0)
    ]

    total_folha = 0
    maior_salario_func = funcionarios[0]

    for f in funcionarios:
        f.exibir_dados()
        sal_calculado = f.calcular_salario()
        print(f" | Salário Final: R$ {sal_calculado:.2f}")

        total_folha += sal_calculado

        if sal_calculado > maior_salario_func.calcular_salario():
            maior_salario_func = f

    
    media_salarial = total_folha / len(funcionarios)
    acima_da_media = sum(1 for f in funcionarios if f.calcular_salario() > media_salarial)

    print("\n--- RESULTADOS GERAIS ---")
    print(f"Total da Folha de Pagamento: R$ {total_folha:.2f}")
    print(f"Funcionário com maior salário: {maior_salario_func.get_nome()} (R$ {maior_salario_func.calcular_salario():.2f})")
    print(f"Média salarial da empresa: R$ {media_salarial:.2f}")
    print(f"Funcionários acima da média: {acima_da_media}")