alunos = ["Alice", "Bruno", "Carla"]
dias = ["Seg", "Ter", "Qua", "Qui"]
reservas = [["Ausente" for _ in dias] for _ in alunos]
print("Preencha com 'S' para presença e 'X' para a ausência:")

for i, aluno in enumerate (alunos) :
    print(f"\nAlunos: {alunos}")
    for j, dia in enumerate(dias) :
        entrada = input(f" {dia}:")
        if entrada.upper() == 'S' :
            reservas[i] [i] = "Presente"

print("\nTabela de reservas:")
print(f"{'Aluno':<10}{''.join([f'{d:<10}'for d in dias])}")
for i, aluno in enumerate (alunos):
    print(f"{aluno:<10} {''.join([f'{res:<10}'for res in reservas [i]])}")