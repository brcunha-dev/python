# condição while
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        print("Você digitou um número inválido")
        break
    if numero % 2 == 0:
        print(f"{numero} é um número par")
    else:
        print(f"{numero} é um número impar")