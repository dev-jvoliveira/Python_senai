distancia = float(input("Digite a distância total percorrida (em km): "))
combustivel = float(input("Digite a quantidade de combustível consumido (em litros): "))

if combustivel > 0:
    consumo_medio = distancia / combustivel
    print(f"O consumo médio de combustível é {consumo_medio:.2f} km/l")
else:
    print("A quantidade de combustível deve ser maior que zero.")
