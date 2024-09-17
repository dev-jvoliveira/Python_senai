def obter_conceito(media):
    if media >= 9.0:
        return 'A'
    elif 7.5 <= media < 9.0:
        return 'B'
    elif 6.0 <= media < 7.5:
        return 'C'
    elif 4.0 <= media < 6.0:
        return 'D'
    else:
        return 'E'


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3) / 3

conceito = obter_conceito(media)

print(f"A média das notas é: {media:.2f}")
print(f"O conceito correspondente é: {conceito}")
