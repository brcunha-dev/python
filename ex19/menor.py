# variáveis
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

# lógica
if (a < b) and (a < c):
    menor = a
elif b < c:
    menor = b
else:
    menor = c

# prints

print(f"Primeiro valor: {a}")
print(f"Segundo valor: {b}")
print(f"Terceiro valor: {c}")
print(f"Menor valor entre os 3 digitados: {menor}")