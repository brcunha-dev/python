soma = 0
cont = 0
idade = int(input("Digite as idades: "))

while idade >= 0:
    soma = soma+idade
    cont = cont+1
    idade = int(input())

if cont == 0:
    print("Impossível calcular")
else:
    media = soma/cont
    print(f"Média {media}")