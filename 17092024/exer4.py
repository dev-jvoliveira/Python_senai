preco_original = float(input("Digite o preço da mercadoria: R$ "))

percentual_desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = preco_original * (percentual_desconto / 100)

preco_a_pagar = preco_original - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")
