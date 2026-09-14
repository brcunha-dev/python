# variáveis
precoUnitario = float(input("Valor unitário do produto R$: "))
quantia = int(input("Quantidade adquirida: "))
dinheiro = float(input("Dinheiro recebido R$: "))

# cálculo de valor do produto
valor = precoUnitario * quantia

# condicional para troco e diferenca
if dinheiro >= valor:
    troco = dinheiro - valor
    print(f"Valor total da compra R$: {valor:.2f}")
    print(f"Troco do cliente R$: {troco:.2f}")
else:
    resto = valor - dinheiro
    print(f"Dinheiro insuficiente, faltam R$: {resto:.2f}")