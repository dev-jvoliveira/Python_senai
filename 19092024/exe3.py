r = 'S'
while r == 'S':
        
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    print("Escolha a operação desejada:")
    print("Soma (+)")
    print("Subtração (-)")
    print("Multiplicação (*)")
    print("Divisão (/)")

    operacao = input("Digite a operação desejada: ")

    if operacao == '+':
        resultado = numero1 + numero2
        print(f"O resultado da soma é: {resultado}")
    elif operacao == '-':
        resultado = numero1 - numero2
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == '*':
        resultado = numero1 * numero2
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, escolha uma das operações listadas.")
    
    r = input('Quer continuar? (S/N): ').upper()
    n = print("Tamo junto, obrigado por utilizar a calculadora")
