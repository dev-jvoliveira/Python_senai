salario_bruto = float(input("Digite o salário bruto: R$ "))

if salario_bruto <= 1903.98:
    ir = 0
    deducao = 0
elif salario_bruto <= 2826.65:
    ir = 0.075
    deducao = 142.80
elif salario_bruto <= 3751.05:
    ir = 0.15
    deducao = 354.80
elif salario_bruto <= 4664.68:
    ir = 0.225
    deducao = 636.13
else:
    ir = 0.257
    deducao = 869.36

imposto_a_pagar = salario_bruto * ir
imposto_retido = max(imposto_a_pagar - deducao, 0)
salario_liquido = salario_bruto - imposto_retido

print()
print('------ RESUMO DOS CÁLCULOS IR ------')
print()
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Faixa de IR: {ir * 100:.1f}%")
print(f"Imposto a Pagar: R$ {imposto_a_pagar:.2f}")
print(f"Imposto Retido: R$ {imposto_retido:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
