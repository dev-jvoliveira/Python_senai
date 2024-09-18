kwh = float(input("Informe a quantidade de kWh consumida: "))
tipo = input("Informe o tipo de instalação (R para Residencial, C para Comercial, I para Industrial): ").upper()


if tipo == 'R':  # Residencial
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65
elif tipo == 'C':  # Comercial
    if kwh <= 2500:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
elif tipo == 'I':  # Industrial
    if kwh <= 10000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
else:
    preco = "Tipo de instalação inválido"


print(f"O valor a pagar é: R$ {preco:.2f}" if isinstance(preco, float) else preco)
