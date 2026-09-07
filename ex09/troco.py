print("Cálculo de troco: ")

# variáveis
preco = float(input("Preço unitário do produto: "))
quantia = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

# cálculos
valorCompra = preco*quantia
troco = dinheiro-valorCompra

print(f"TROCO: R$: {troco:.2f}")