def calcular_peso_ideal():
    
    nome = input("Digite o seu nome: ")
    altura = float(input("Digite a sua altura (em metros): "))
    sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()
    
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido. Utilize 'M' para masculino ou 'F' para feminino.")
        return
    
    print(f"\nNome: {nome}")
    print(f"Altura: {altura:.2f} m")
    print(f"Peso Ideal: {peso_ideal:.2f} kg")

calcular_peso_ideal()
