import math
print("Vamos calcular a fórmula de Baskara!")

# variaveis
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de c: "))
delta = (b**2)-4*a*c
if delta<=0:
    print("Delta menor que 0, fim do programa")
else:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)

print(f"O valor de X1 é: {x1}")
print(f"O valor de X2 é: {x2}")    
