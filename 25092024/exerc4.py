def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Digite o comprimento da base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
area = calcular_area_triangulo(base, altura)
print(f"A área do triângulo com base {base} e altura {altura} é: {area:.2f}")
