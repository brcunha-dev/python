soma = 0
numero = int(input("Digite um número: "))
soma = soma+numero

while soma < 100:
    numero = int(input("Digite outro número: "))
    soma = soma+numero
    print(f"A soma atual é: {soma}")


print(f"O limite da soma foi atingido: {soma}")
