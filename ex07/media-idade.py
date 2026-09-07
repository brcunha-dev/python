print("Calculando a média de idade de duas pessoas")

# variáveis
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

media = (idade1+idade2) / 2

print("Dados da primeira pessoa: ")
print(f"Nome: {nome1}")
print(f"Idade: {idade1}")

print("Dados da segunda pessoa: ")
print(f"Nome: {nome2}")
print(f"Idade: {idade2}")

print(f"A média de idade das duas pessoas é: {media:.1f}")
