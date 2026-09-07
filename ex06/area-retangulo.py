import math
print("Vamos calcular os valores de um retângulo")

# variáveis
base = float(input("Digite a base do retângulo"))
altura = float(input("Digite a altura do retângulo"))

# contas
area = altura*base
perimetro = (2*base)+(2*altura)
diagonal = math.sqrt(base**2+altura**2)

print(f"A área do retângulo é: {area}")
print(f"O perimetro do retângulo é {perimetro}")
print(f"A diagonal do retângulo é: {diagonal}")