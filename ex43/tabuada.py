import time  

while True:

    numero = int(input("Informe um número: "))

    if numero == 0:
        print("Número inválido")
        break

    contador = 1

    while contador <= 10:
        resultado = numero*contador
        print(f"{numero} * {contador} = {resultado}")

        time.sleep(0.5)
        
        contador = contador + 1