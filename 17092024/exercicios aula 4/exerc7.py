idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso em kg: "))
horas_sono = float(input("Quantas horas você dormiu nas últimas 24 horas? "))


if 16 <= idade <= 69 and peso > 50 and horas_sono >= 6:
    print("Você está apto(a) para doar sangue.")
else:
    print("Você não está apto(a) para doar sangue.")
