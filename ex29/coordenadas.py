# variáveis
x = float(input("Informe o valor de X: "))
y = float(input("Informe o valor de Y: "))

if (x > 0) and (y > 0):
    print("Ponto em Q1")
elif (x < 0) and (y > 0):
    print("Ponto em Q2")
elif (x < 0) and (y < 0):
    print("Ponto em Q3")
elif (x > 0) and (y < 0):
    print("Ponto em Q4")
elif (x == 0) and (y > 0):
    print("Ponto em Y")
elif (x > 0) and (y == 0):
    print("Ponto em X")
else:
    print("Ponto alocado na Origem do plano!")