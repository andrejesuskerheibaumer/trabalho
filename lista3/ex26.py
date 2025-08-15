def eleicao():
    candidatos = {
        "Candidato A": 0,
        "Candidato B": 0,
        "Candidato C": 0
    }
    
    total_participantes = int(input("Digite o número total de participantes: "))
    
    for i in range(total_participantes):
        print(f"\nVotante {i + 1}:")
        print("1 - Candidato A")
        print("2 - Candidato B")
        print("3 - Candidato C")
        
        voto = int(input("Digite o número do candidato em que você deseja votar: "))
        
        if voto == 1:
            candidatos["Candidato A"] += 1
        elif voto == 2:
            candidatos["Candidato B"] += 1
        elif voto == 3:
            candidatos["Candidato C"] += 1
        else:
            print("Voto inválido. Nenhum voto contabilizado para este eleitor.")

    print("\nResultado da Eleição:")
    print(f"Candidato A: {candidatos['Candidato A']} votos")
    print(f"Candidato B: {candidatos['Candidato B']} votos")
    print(f"Candidato C: {candidatos['Candidato C']} votos")

eleicao()