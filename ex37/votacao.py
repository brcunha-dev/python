while True:
# variáveis
    idade = int(input("Informe sua idade: (Ou um número negativo para sair.)"))

    if idade < 0:
        print("Programa encerrado")
        break

    if idade < 16:
        print("Você não pode votar!")
    else:
        print("Você pode votar!")

