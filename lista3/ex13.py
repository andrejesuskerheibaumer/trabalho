# Solicita a entrada do usuário
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Variável para armazenar o resultado
resultado = 1

# Calcula a potência manualmente
for _ in range(expoente):
    resultado *= base

# Mostra o resultado
print(f"{base} elevado a {expoente} é {resultado}")
