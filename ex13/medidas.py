print("Cálculo de área de várias figuras geométricas")

# variáveis
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

# cálculos
areaQuadrado = a**2
areaTriangulo = (b*a)/2
areaTrapezio = (a+b)/2*c

print(f"Área do quadrado: {areaQuadrado:.2f}")
print(f"Área do triângulo: {areaTriangulo:.2f}")
print(f"Área do trapézio: {areaTrapezio:.2f}")