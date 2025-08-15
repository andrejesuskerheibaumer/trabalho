def soma_harmonica(n):
    H = 0
    for i in range(1, n + 1):
        H += 1 / i
    return H

# Solicita ao usuário o valor de N
N = int(input("Digite o valor de N: "))
resultado = soma_harmonica(N)
print(f"O valor da soma harmônica H para N={N} é: {resultado}")
