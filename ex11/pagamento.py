print("Cálculo de horas trabalhadas")

# variáveis
nome = input("Nome: ")
valorHora = float(input("Valor por hora: "))
horaTrabalhada = float(input("Horas trabalhadas: "))

# cálculo
pagamento = valorHora * horaTrabalhada

print(f"O pagamento para {nome} deve ser de R$: {pagamento:.2f}")