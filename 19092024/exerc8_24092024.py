while True:

    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    
    print('\nEscolha uma opção: ')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Menor')
    print('[5] Dividir')
    print('[6] Subtrair')
    print('[7] Sair do programa')

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        print('Resultado: ', valor1 + valor2)  
    elif opcao == 2:
        print('Resultado: ', valor1 * valor2)
    elif opcao == 3:
        if valor1 > valor2:
            print('Maior valor: ', valor1)
        else:
            print('Maior valor: ', valor2)
    elif opcao == 4:
        if valor1 < valor2:
            print('Menor valor: ', valor1)
        else:
            print('Menor valor: ', valor2)
    elif opcao == 5:
        if valor2 != 0:
            print('Resultado: ', valor1 / valor2)
        else:
            print('Erro: Divisão por zero!')
    elif opcao == 6:
        print('Resultado: ', valor1 - valor2)
    elif opcao == 7:
        print('Saindo do programa...')
    else:
        print('Opção inválida! Tente novamente.')
    
    
    
    
    
    
