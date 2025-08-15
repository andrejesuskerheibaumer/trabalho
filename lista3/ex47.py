def calcular_media_ginasta():
    # Recebendo o nome do ginasta
    nome_ginasta = input("Digite o nome do ginasta: ")

    # Listas para armazenar as notas
    notas = []

    # Recebendo as notas dos jurados
    for i in range(7):
        nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)

    # Encontrar a melhor e a pior nota
    melhor_nota = max(notas)
    pior_nota = min(notas)

    # Remover a melhor e a pior nota
    notas.remove(melhor_nota)
    notas.remove(pior_nota)

    # Calcular a média das notas restantes
    media = sum(notas) / len(notas)

    # Exibindo os resultados
    print("\nResultado final:")
    print(f"Atleta: {nome_ginasta}")
    print(f"Melhor nota: {melhor_nota:.1f}")
    print(f"Pior nota: {pior_nota:.1f}")
    print(f"Média: {media:.2f}")

# Executar a função
calcular_media_ginasta()