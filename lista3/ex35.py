def eh_primo(num):
    """Função para verificar se um número é primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def listar_numeros_primos(limite):
    """Função para listar números primos até o limite especificado."""
    primos = []
    for num in range(2, limite + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

def main():
    # Solicita um número inteiro do usuário
    limite = int(input("Digite um número inteiro para encontrar números primos até esse limite: "))
    
    # Gera a lista de números primos
    primos = listar_numeros_primos(limite)
    
    # Exibe a lista de números primos
    print(f"Números primos entre 1 e {limite}: {primos}")

