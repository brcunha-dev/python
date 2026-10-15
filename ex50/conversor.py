while True:
    c = float(input("Informe a temperatura em Celsius: "))

    f = 9*c/5+32
    print(f"A temperatura em Fahrenheit é de {f}")

    resp = (input("Deseja continuar (s/n): "))

    if resp == "n":
        break

