ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento

idade_meses = idade_anos * 12

idade_dias = idade_anos * 365.25

idade_semanas = idade_dias / 7

print("A idade em anos é:", idade_anos)
print("A idade em meses é:", idade_meses)
print("A idade em dias é:", round(idade_dias))
print("A idade em semanas é:", round(idade_semanas))
