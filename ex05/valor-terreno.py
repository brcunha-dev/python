print("Vamos calcular o valor de um terreno e sua área")

# variaveis
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
metroQuadrado = float(input("Digite o valor do metro quadrado do terreno: "))
# variaveis recebendo os calculos
area = largura*comprimento
preco = area*metroQuadrado

print(f"A área do terreno é de: {area} m²")
print(f"O preço do terreno é de R$: {preco}")