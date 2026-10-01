while True:
    n = int(input("Informe quantos números serão digitados (0 para finalizar:) "))

    if n == 0:
        print("Programa encerrado")
        break

    soma = 0

    for i in range (0, n):
        x = int(input("Digite um número: "))

        soma = soma+x

    print(f"Soma = {soma}")

