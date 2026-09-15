# variaveis
salario = float(input("Informe o salário: "))

# if
if salario <= 1000:
    porcentagem = 20
elif salario <= 3000:
    porcentagem = 15
elif salario <= 8000:
    porcentagem = 10
else:
    porcentagem = 5

# cálculo
aumento = salario*porcentagem/100
novoSalario = aumento+salario

print(f"Aumento: R$: {aumento:.2f}")
print(f"Novo salário: R$: {novoSalario:.2f}")
print(f"Porcentagem: {porcentagem}%")