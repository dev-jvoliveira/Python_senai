mercadoria = float(input('Digite o valor do produto: '))

valor_desconto = mercadoria * 0.10
valor_novo = mercadoria - valor_desconto

print(f'Você teve um desconto de R$: {valor_desconto:.2f}')
print(f'O Valor do produto com desconto foi de: {valor_novo:.2f}')
