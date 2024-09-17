limite_peso = 50  
multa_por_quilo_excedente = 4.00  

def calcular_multa(peso):
    if peso > limite_peso:
        excesso = peso - limite_peso
        multa = excesso * multa_por_quilo_excedente
    else:
        excesso = 0
        multa = 0
    return excesso, multa

peso_peixes = float(input("Digite o peso de peixes trazidos por João (em quilos): "))
excesso, multa = calcular_multa(peso_peixes)

print(f"Excesso de peso: {excesso} kg")
print(f"Multa a ser paga: R$ {multa:.2f}")
