def calcular_area_quadrado(lado):
    area = lado ** 2
    return area

lado = float(input("Digite o comprimento do lado do quadrado: "))
area = calcular_area_quadrado(lado)
print(f"A área do quadrado com lado {lado} é: {area:.2f}")
