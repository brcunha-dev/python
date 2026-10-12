while True:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))

    if x == 0:
        print("Programa encerrado")
        break

    if x > y:
        troca = x
        x = y
        y = troca

    soma = 0
    for i in range(x+1, y-1):
        if i % 2 != 0:
            soma = soma+i

    print(f"A soma dos números impares é: {soma}")



