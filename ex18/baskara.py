import math

# variáveis
a = float(input("Coeficiente A: "))
b = float(input("Coeficiente B: "))
c = float(input("Coeficiente C: "))

# cálcula delta
delta = (b**2) -4 * a * c

# condicional a = 0 ou delta < 0
if a == 0 or delta < 0:
    print("Equação sem raizes reais!")
else:
    x1 = (-b + math.sqrt(delta)) / (2 *a)
    x2 = (-b - math.sqrt(delta)) / (2 *a)

print(f"Valor de x1: {x1:.2f}")
print(f"Valor de x2: {x2:.2f}")