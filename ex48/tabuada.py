import time

while True:
    # Escolha do número
    n = int(input("Informe o valor que deseja a tabuada ou 0 para sair: "))

    # COndição para encerramento
    if n == 0:
        print("Programa encerrado")
        break

    # Lógica da tabuada
    for i in range(1, 11):

        time.sleep(.5)
        produto = n*i

        print(f"{n} x {i} = {produto}")