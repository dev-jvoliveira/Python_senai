velocidade = float(input("Informe a velocidade do carro (em km/h): "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5
    print(f"Você foi multado! A velocidade excedeu o limite de 80 km/h.")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade.")
