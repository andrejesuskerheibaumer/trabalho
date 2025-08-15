# Solicita ao usuário um número de 1 a 10
numero = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))

# Verifica se o número está no intervalo permitido
if 1 <= numero <= 10:
    print(f"\nTabuada de {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
else:
    print("Número inválido! Digite um número inteiro entre 1 e 10.")
