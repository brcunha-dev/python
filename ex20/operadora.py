# variáveis
minutos = int(input("Informe os minutos utilizados: "))
valorPago = 50.0

# condicao
if minutos > 100:
    valorPago = valorPago + 2 * (minutos - 100)

print(f"Minutos usados: {minutos}")
print(f"Valor a pagar R$: {valorPago:.2f}")