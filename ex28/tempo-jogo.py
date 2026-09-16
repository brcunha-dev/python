horaInicial = int(input("Digite a hora inicial: "))
horaFinal = int(input("Digite a hora final: "))

if horaInicial < horaFinal:
    duracao = horaFinal - horaInicial
else:
    duracao = (24 - horaInicial) + horaFinal

print(f"Tempo de jogo: {duracao} horas")