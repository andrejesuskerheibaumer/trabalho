while True:
    # Entrada com validação
    while True:
        n = int(input("Digite um número inteiro positivo menor que 16: "))
        if 1 <= n < 16:
            break
        else:
            print("Valor inválido! Digite novamente.")

    fatorial = 1
    print(f"{n}! =", end=" ")

    for i in range(n, 0, -1):
        fatorial *= i
        print(i, end=" x " if i > 1 else " = ")

    print(fatorial)

    # Pergunta se deseja continuar
    continuar = input("Deseja calcular outro fatorial? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa encerrado.")
        break
