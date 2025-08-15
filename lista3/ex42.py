def contar_intervalos():
    # Inicialização dos contadores
    contagem_0_25 = 0
    contagem_26_50 = 0
    contagem_51_75 = 0
    contagem_76_100 = 0

    while True:
        # Leitura do número
        numero = float(input("Digite um número positivo (ou um número negativo para sair): "))

        # Verificação se o número é negativo para encerrar o loop
        if numero < 0:
            break
        
        # Contagem conforme o intervalo
        if 0 <= numero <= 25:
            contagem_0_25 += 1
        elif 26 <= numero <= 50:
            contagem_26_50 += 1
        elif 51 <= numero <= 75:
            contagem_51_75 += 1
        elif 76 <= numero <= 100:
            contagem_76_100 += 1
        else:
            print("Número fora do intervalo considerado (0-100).")

    # Exibindo os resultados
    print(f"Números no intervalo [0-25]: {contagem_0_25}")
    print(f"Números no intervalo [26-50]: {contagem_26_50}")
    print(f"Números no intervalo [51-75]: {contagem_51_75}")
    print(f"Números no intervalo [76-100]: {contagem_76_100}")