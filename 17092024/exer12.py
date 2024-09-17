salario_minimo = float(input("Digite o valor do salário mínimo: "))

salario_funcionario = float(input("Digite o valor do salário do funcionário: "))

quantidade_salarios_minimos = salario_funcionario / salario_minimo

print("O funcionário ganha o equivalente a {:.2f} salários mínimos.".format(quantidade_salarios_minimos))
