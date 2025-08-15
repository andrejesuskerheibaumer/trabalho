def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar um número inteiro ao usuário
try:
    numero_inferido = int(input("Digite um número inteiro: "))
    if eh_primo(numero_inferido):
        print(f"{numero_inferido} é um número primo.")
    else:
        print(f"{numero_inferido} não é um número primo.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")