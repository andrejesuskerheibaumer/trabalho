def analisar_temperaturas():
    temperaturas = []
    
    while True:
        temperatura = input("Digite uma temperatura (ou 'sair' para encerrar): ")
        
        if temperatura.lower() == 'sair':
            break
        
        try:
            temperaturas.append(float(temperatura))
        except ValueError:
            print("Por favor, insira um número válido ou 'sair' para encerrar.")
    
    if temperaturas:
        menor = min(temperaturas)
        maior = max(temperaturas)
        media = sum(temperaturas) / len(temperaturas)
        
        print(f"\nMenor temperatura: {menor:.2f}°C")
        print(f"Maior temperatura: {maior:.2f}°C")
        print(f"Média das temperaturas: {media:.2f}°C")
    else:
        print("Nenhuma temperatura foi registrada.")

analisar_temperaturas()
