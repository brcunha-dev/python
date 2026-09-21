# variáveis
x = int(input("Digite um números: "))
y = int(input("Digite outro número: "))

# condição
while x != y:
    if x<y:
        print("Crescente")
    else:
        print("Decrescente")

    x = int(input("Digite outro número: "))
    y = int(input("Digite outro número: "))