codigo = int(input("Informe o código do produto: "))
quantidade = int(input("Informe a quantia comprada: "))

match codigo:
    case 1:
        valorPago = 5 * quantidade
    case 2:
        valorPago = 3.50 * quantidade
    case 3:
        valorPago = 4.80 * quantidade
    case 4:
        valorPago = 8.90 * quantidade
    case 5:
        valorPago = 7.32 * quantidade

print(f"Valor a pagar: R$: {valorPago:.2f}")