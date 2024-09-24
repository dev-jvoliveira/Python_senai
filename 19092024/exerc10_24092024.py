valor_compra = float(input('Digite o valor da compra: '))

if valor_compra <= 100:
    forma_pagamento = 'dinheiro'
elif 100 < valor_compra <= 300:
    forma_pagamento = 'cartão de débito'
else:
    forma_pagamento = 'cartão de crédito'
print(f'Você deve pagar em {forma_pagamento}')
        
