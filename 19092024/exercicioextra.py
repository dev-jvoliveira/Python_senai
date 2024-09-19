def calcular_ir(salario_bruto):
    if salario_bruto <= 1903.98:
        percentual = 0
        deducao = 0
    elif salario_bruto <= 2826.65:
        percentual = 0.075
        deducao = 142.80
    elif salario_bruto <= 3751.05:
        percentual = 0.15
        deducao = 354.80
    elif salario_bruto <= 4664.68:
        percentual = 0.225
        deducao = 636.13
    else:
        percentual = 0.275
        deducao = 869.36

    imposto_a_pagar = salario_bruto * percentual
    imposto_retido = max(imposto_a_pagar - deducao, 0)
    salario_liquido = salario_bruto - imposto_retido - imposto_a_pagar

    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Faixa de IR: {percentual * 100:.1f}%")
    print(f"Imposto de Renda a Pagar: R$ {imposto_a_pagar:.2f}")
    print(f"Valor Padrão: R$ {deducao:.2f}")
    print(f"Imposto Retido na Fonte: R$ {imposto_retido:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

salario_bruto = float(input("Digite o salário bruto: R$ "))
calcular_ir(salario_bruto)
