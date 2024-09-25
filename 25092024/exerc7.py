def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_final = custo + imposto
    return custo_final

taxa_imposto = float(input("Digite a taxa de imposto (em %): "))
custo = float(input("Digite o custo do item: "))
custo_com_imposto = somaImposto(taxa_imposto, custo)
print(f"O custo do item com imposto é: {custo_com_imposto:.2f}")
