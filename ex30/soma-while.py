# Soma com while

# variáveis
x = int(input("Digite o primeiro número: "))

# condição de execução
soma = 0

while x != 0:
    soma = soma + x
    x = int(input("Digite outro número: "))

print(f"Soma: {soma}")