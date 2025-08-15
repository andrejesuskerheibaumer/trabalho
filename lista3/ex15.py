# Solicita ao usuário o número de termos
n = int(input("Digite o número de termos da série de Fibonacci: "))

# Primeiros dois termos da série
a, b = 1, 1

print("Série de Fibonacci:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

