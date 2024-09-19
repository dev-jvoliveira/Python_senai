impares = 0
pares = 0

num = int(input('Digite um numero ou digite 0 para parar: '))

while num != 0:

    if num % 2 == 1:
        impares += 1
    else:
        pares += 1
    num = int(input('Digite um numero ou digite 0 para parar: '))

print ('Numeros impares contam: ', impares)
print ('Numeros pares contam: ', pares)
