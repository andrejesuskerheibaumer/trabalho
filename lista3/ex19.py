# Solicita o número com validação
while True:
    n = int(input("Digite um número inteiro entre 0 e 1000: "))
    if 0 <= n <= 1000:
        break
    else:
        print("Valor inválido! Digite um número entre 0 e 1000.")

fatorial = 1

print(f"{n}! =", end=" ")

# Calcula o fatorial e exibe passo a passo
for i in range(n, 0, -1):
    fatorial *= i
    print(i, end=" x " if i > 1 else " = ")

print(fatorial)
