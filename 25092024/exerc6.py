def ver_numero(valor):
    if valor > 0:
        return 'P'
    else:
        return 'N'

numero=float(input('Digite um numero: '))
resultado= ver_numero(numero)
print(f'O resultado é: {resultado}')
