# Solicita o número
n = int(input("Digite um número inteiro: "))

# Números menores que 2 não são primos
if n < 2:
    print(f"{n} não é um número primo.")
else:
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            divisor = i
            break

    if primo:
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo. Ele é divisível por {divisor}.")
