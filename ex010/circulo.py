import math

print("Calculando a área de um círculo")

# variáveis
raio = float(input("Digite o valor do raio do círculo: "))

# cálculo
area = math.pi*(raio**2)

print(f"A área do círculo é de: {area:.2f}")