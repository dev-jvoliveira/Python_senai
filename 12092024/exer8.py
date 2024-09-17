def calcular_area_quadrado():
    
    lado = float(input("Digite o comprimento do lado do quadrado: "))
    
    area = lado ** 2
    
    dobro_area = area * 2
    
    print(f"\nÁrea do quadrado: {area:.2f}")
    print(f"Dobro da área: {dobro_area:.2f}")

calcular_area_quadrado()
