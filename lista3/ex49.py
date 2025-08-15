# Solicita ao usuário o número de termos
n = int(input("Digite o número de termos da série: "))

# Inicializa a soma
soma = 0

# Calcula cada termo da série e atualiza a soma
for i in range(1, n + 1):
    # A sequência dos denominadores é 1, 3, 5, 7,..., que é gerada pela fórmula (2 * i - 1)
    denominador = 2 * i - 1
    termo = i / denominador
    soma += termo
    # Mostra o termo calculado
    print(f"{i}/{denominador}", end=" ")
    if i < n:
        print("+", end=" ")
print()  # Quebra de linha após a impressão dos termos

# Imprime a soma final
print(f"Soma da série para {n} termos: {soma:.4f}")