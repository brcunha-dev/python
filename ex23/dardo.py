# variáveis
distancia1 = float(input("Digite a primeira distancia: "))
distancia2 = float(input("Digite a segunda distancia: "))
distancia3 = float(input("Digite a terceira distancia: "))

# condição
if (distancia1 > distancia2) and (distancia1 > distancia3):
    maior = distancia1
    print(f"Maior distancia: {maior:.2f}")
elif distancia2 > distancia3:
    maior = distancia2
    print(f"Maior distancia: {maior:.2f}")
else:
    maior = distancia3
    print(f"Maior distancia: {maior:.2f}")
