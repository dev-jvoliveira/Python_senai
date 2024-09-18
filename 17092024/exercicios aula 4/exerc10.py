valor = float(input("Digite o valor da compra: R$ "))

if valor <= 100:
    print("A forma de pagamento deve ser: dinheiro.")
elif valor <= 300:
    print("A forma de pagamento deve ser: cartão de débito.")
else:
    print("A forma de pagamento deve ser: cartão de crédito.")
