peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso/(altura * altura)

print(f"O seu IMC é: ", imc)

if imc < 19:
    print("Classificação: Muito Magro")
elif 19 <= imc < 25:
    print("Classificação: Normal")
elif 25 <= imc < 30:
    print("Classificação: Sobre Peso")
elif 30 <= imc < 40:
    print("Classificação: Obeso")
else:
    print("Classificação: Obesidade Grave")
