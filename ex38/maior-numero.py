while True:
    numero1 = int(input("Digite o primeiro número: (Ou número negativo para encerrar)" ))

    # condição de parada
    if numero1 < 0:
        print("Programa encerrado!")
        break

    numero2 = int(input("Digite o segundo número: "))

    if numero1 > numero2:
        print(f"{numero1} é o maior dos dois.")
    elif numero1 == numero2:
        print("Os números digitados são iguais!")
    else:
        print(f"{numero2} é o maior dos dois.")
