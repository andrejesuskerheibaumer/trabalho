def main():
    # Inicializa as variáveis para armazenar o número do aluno e a altura
    mais_alto_num = None
    mais_alto_altura = 0
    mais_baixo_num = None
    mais_baixo_altura = float('inf')

    for i in range(10):  # Para 10 alunos
        # Solicita a entrada dos dados
        numero_aluno = int(input(f"Digite o número do aluno {i + 1}: "))
        altura = float(input(f"Digite a altura do aluno {numero_aluno} (em cm): "))

        # Verifica se o aluno é o mais alto
        if altura > mais_alto_altura:
            mais_alto_altura = altura
            mais_alto_num = numero_aluno
        
        # Verifica se o aluno é o mais baixo
        if altura < mais_baixo_altura:
            mais_baixo_altura = altura
            mais_baixo_num = numero_aluno

    # Exibe os resultados
    print(f"\nAluno mais alto: Número {mais_alto_num}, Altura {mais_alto_altura} cm")
    print(f"Aluno mais baixo: Número {mais_baixo_num}, Altura {mais_baixo_altura} cm")
