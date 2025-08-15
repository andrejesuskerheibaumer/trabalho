# Solicita um número inteiro positivo ao usuário
numero = input("Digite um número inteiro positivo: ")

# Verifica se o número é positivo e se é um inteiro
if numero.isdigit():
    # Inverte o número usando slicing
    numero_invertido = numero[::-1]
    
    # Mostra o número invertido
    print(f"=> {numero_invertido}")
else:
    print("Por favor, digite um número inteiro positivo.")