# 1
print("####### Exercício 1:")

fat = input("Digite o faturamento:")
fat = fat.replace("R$", "").replace(".", "").replace(",", ".")
fat_numerico = float(fat)
perc_imposto = 0.15
imposto = fat_numerico * perc_imposto
print(f"Imposto pago: R${imposto:,.2f}")