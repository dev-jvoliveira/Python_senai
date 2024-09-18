numero = int(input("Digite um número de 1 a 12: "))

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if 1 <= numero <= 12:
    print(f"O mês correspondente é: {meses[numero - 1]}")
else:
    print("Não existe mês com este número.")
