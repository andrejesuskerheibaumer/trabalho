def calcular_media_alunos():
    num_turmas = int(input("Digite a quantidade de turmas: "))
    total_alunos = 0

    for i in range(num_turmas):
        alunos = int(input(f"Digite a quantidade de alunos na turma {i + 1} (máximo 40): "))
        
        if alunos > 40:
            print("Número de alunos não pode ser maior que 40. Este valor será desconsiderado.")
            continue
        
        total_alunos += alunos

    if num_turmas > 0:
        media_alunos = total_alunos / num_turmas
        print(f"A média de alunos por turma é: {media_alunos:.2f}")
    else:
        print("Nenhuma turma foi registrada.")

calcular_media_alunos()
