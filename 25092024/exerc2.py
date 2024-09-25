def eh_multiplo(num1, num2):
    if num2 == 0:
        return False  
    return num1 % num2 == 0

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = eh_multiplo(numero1, numero2)
if resultado:
    print(f"{numero1} é múltiplo de {numero2}.")
else:
    print(f"{numero1} não é múltiplo de {numero2}.")
