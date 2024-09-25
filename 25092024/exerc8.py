def eleicao(idade):
    if idade < 16:
        return 'Não pode votar'
    elif 18 <= idade <= 65:
        return 'Eleito obrigatorio'
    elif (16 <= idade < (18) or (idade > 65)):
          return 'Eleitor facultativo'
idade = int(input('Digite a idade: '))
resultado = eleicao(idade)
print(f'A sua classe eleitoral é: {resultado}')
