# Solicita o número
n = int(input("Digite um número inteiro para calcular o fatorial: "))

fatorial = 1

print(f"{n}! =", end=" ")

# Calcula o fatorial e exibe o cálculo passo a passo
for i in range(n, 0, -1):
    fatorial *= i
    print(i, end=" x " if i > 1 else " = ")

print(fatorial)
