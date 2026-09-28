import time

while True:

    numero = int(input("Digite um número: "))

    if numero == 0:
        print("Programa encerrado!")
        break

    contador = numero

    while contador > 0:

        time.sleep(.5)
        contador = contador-1
        print(f"{contador}")