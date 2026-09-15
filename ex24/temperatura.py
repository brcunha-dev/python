unidade = (input("Você vai usar a temperatura em qual escala (c/f)?: "))

if unidade == "f":
    f = float(input("Informe a temperatura em Fahrenheit: "))
    c = 5/9*(f-32)
    print(f"A temperatura em Celsius é: {c:.2f}")
else:
    c = float(input("Informe a temperatura em Celsius: "))
    f = 9*c/5+32
    print(f"A temperatura em Fahrenheit é: {f:.2f}")