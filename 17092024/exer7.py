def calcular_salario():
    
    ganho_por_hora = float(input("Quanto você ganha por hora? R$ "))
    horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
    
    salario_bruto = ganho_por_hora * horas_trabalhadas
    
    desconto_ir = salario_bruto * 0.11
    desconto_inss = salario_bruto * 0.08
    desconto_sindicato = salario_bruto * 0.05
    
   
    salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
    
    
    print(f"\n+ Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"IR (11%): R$ {desconto_ir:.2f}")
    print(f"INSS (8%): R$ {desconto_inss:.2f}")
    print(f"Sindicato (5%): R$ {desconto_sindicato:.2f}")
    print(f"= Salário líquido: R$ {salario_liquido:.2f}")


calcular_salario()
