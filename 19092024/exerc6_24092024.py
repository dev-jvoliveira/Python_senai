soma_pares = 0

for i in range(6):
    numero = int(input(f'Digite o {i+1}° número: '))

    if numero % 2 == 0:
        soma_pares += numero
print('A soma dos números pares é: ', soma_pares)
