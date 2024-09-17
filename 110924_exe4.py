def pode_se_alistar(idade, sexo):

    if idade >= 18:
        
        if sexo.lower() == 'm':
            return "Pode se alistar."
        else:
            return "Não pode se alistar."
    else:
        return "Não pode se alistar"

idade = int(input("Digite a idade da pessoa: "))
sexo = input("Digite o sexo da pessoa (m/f): ").strip().lower()

resultado = pode_se_alistar(idade, sexo)
print(resultado)
