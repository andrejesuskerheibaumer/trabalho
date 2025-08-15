# Função para calcular a média aritmética
def calcula_media(notas):
    return sum(notas) / len(notas)

def main():
    # Solicita ao usuário o número de notas
    n = int(input("Quantas notas você deseja inserir? "))

    # Inicializa uma lista para armazenar as notas
    notas = []

    # Laço para receber as notas do usuário
    for i in range(n):
        nota = float(input(f"Insira a nota {i + 1}: "))
        notas.append(nota)

    # Calcula a média
    media = calcula_media(notas)

    # Exibe o resultado
    print(f"A média aritmética das notas é: {media:.2f}")

