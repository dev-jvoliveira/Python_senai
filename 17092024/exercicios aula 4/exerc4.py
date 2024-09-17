valor_casa = float(input("Informe o valor da casa a comprar (em R$): "))

salario = float(input("Informe o seu salário (em R$): "))

anos = int(input("Informe a quantidade de anos para pagar o empréstimo: "))

meses = anos * 12

prestacao_mensal = valor_casa / meses

percentual_salario = salario * 0.30

if prestacao_mensal > percentual_salario:
    print(f"Empréstimo negado! A prestação mensal de R$ {prestacao_mensal:.2f} excede 30% do seu salário.")
else:
    print(f"Empréstimo aprovado! A prestação mensal será de R$ {prestacao_mensal:.2f}.")
