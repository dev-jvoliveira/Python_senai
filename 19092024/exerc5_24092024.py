numero = int(input('Digite um numero para ver sua tabuada: '))

print(f'Tabuada de {numero}: ')
for i in range(1,11):
    print(f'{numero} x {i:2} = {numero * i}')
