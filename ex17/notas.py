nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

notaFinal = (nota1 + nota2) / 2

if notaFinal < 60:
    print(f"Nota final:{notaFinal:.2f} - Reprovado")
else:
    print(f"Nota final: {notaFinal:.2f} - Aprovado")