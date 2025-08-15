def calcular_media_saltos():
    while True:
        nome_atleta = input("Informe o nome do atleta (ou pressione Enter para sair): ")
        if not nome_atleta:
            break
        
        saltos = []
        
        for i in range(1, 6):
            salto = float(input(f"{i}° Salto: "))
            saltos.append(salto)
        
        melhor_salto = max(saltos)
        pior_salto = min(saltos)
        
        # Remover melhor e pior salto
        saltos.remove(melhor_salto)
        saltos.remove(pior_salto)
        
        media = sum(saltos) / len(saltos)
        
        print(f"\nAtleta: {nome_atleta}\n")
        for i in range(5):
            print(f"{i+1}° Salto: {saltos[i] if i < 3 else ''} m")
        
        print(f"\nMelhor salto: {melhor_salto} m")
        print(f"Pior salto: {pior_salto} m")
        print(f"Média dos demais saltos: {media:.1f} m")
        
        print(f"\nResultado final:\n{nome_atleta}: {media:.1f} m\n")

# Chamar a função
calcular_media_saltos()