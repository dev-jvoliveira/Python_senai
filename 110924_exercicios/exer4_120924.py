par = None
impar = None

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    par = numero
else:
    impar = numero

print("Número par:", par if par is not None else "Nenhum número par")
print("Número ímpar:", impar if impar is not None else "Nenhum número ímpar")
