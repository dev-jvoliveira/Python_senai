def calcular_saldo_restante(salario, conta1, conta2):
    multa = 0.02
    multa_conta1 = conta1 * multa
    multa_conta2 = conta2 * multa
    
    total_conta1 = conta1 + multa_conta1
    total_conta2 = conta2 + multa_conta2
    
    total_pagar = total_conta1 + total_conta2
    saldo_restante = salario - total_pagar
    
    return saldo_restante

salario = float(input("Digite o salário do João: R$ "))
conta1 = float(input("Digite o valor da primeira conta: R$ "))
conta2 = float(input("Digite o valor da segunda conta: R$ "))

saldo_restante = calcular_saldo_restante(salario, conta1, conta2)
print(f"Após pagar as contas com multa, o saldo restante do João é: R$ {saldo_restante:.2f}")
