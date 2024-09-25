def sua_nota(nota):
    if nota < 3:
        return'Conceito E'
    elif 3 <= nota <= 5:
        return'Conceito D'
    elif 6 <= nota <= 7:
        return'Conceito C'
    elif 8 <= nota <= 9:
        return'Conceito B'
    elif nota == 10:
        return'Conceito A'
    else:
        return'Nota inválida'

nota = float(input('Digite a nota do aluno(0 a 10): '))
resultado = sua_nota(nota)
print(f'O Conceito do aluno é: {resultado}')
