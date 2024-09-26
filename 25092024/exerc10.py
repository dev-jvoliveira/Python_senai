def impar(a, b):
    soma=0
    for numero in range(a, b + 1):
        if numero %2!= 0:
            soma += numero
    return soma
a= int(input('Digite o valor de A: '))
b= int(input('Digite o valor de B: '))

calc= impar(a, b)
print(f'A soma dos números impares de {a} e {b} é: {calc}')
