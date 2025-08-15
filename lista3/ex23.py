# Solicita o valor de N
N = int(input("Digite um número inteiro N: "))

total_divisoes = 0  # Contador de divisões
primos = []         # Lista para armazenar os números primos

# Percorre de 2 até N (1 não é primo)
for num in range(2, N + 1):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        total_divisoes += 1  # Conta a tentativa de divisão
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)

# Mostra resultados
print(f"Números primos entre 1 e {N}: {primos}")
print(f"Total de divisões executadas: {total_divisoes}")
