n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

if n1 != 0 and n2 != 0:
    media = (n1 + n2) / 2
    print("A media é: ", media)

else:
    print("Não foi possivel calcular, um dos valores é igual a zero. ")
