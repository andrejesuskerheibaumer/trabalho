def calcular_salario_atual(salario_inicial):
    # Salário inicial
    salario = salario_inicial
    
    # Aumento de 1,5% em 1996
    aumento = 1.5 / 100
    salario *= (1 + aumento)
    
    # Aumentos de 1997 até o ano atual
    ano_inicial = 1996
    ano_atual = 2023  # você pode atualizar isso para o ano atual
    for ano in range(ano_inicial + 1, ano_atual + 1):
        aumento *= 2  # o aumento dobrou a cada ano
        salario *= (1 + aumento)

    return salario

def main():
    # Solicita ao usuário o salário inicial do funcionário
    salario_inicial = float(input("Digite o salário inicial do funcionário: R$ "))
    
    # Calcula o salário atual
    salario_atual = calcular_salario_atual(salario_inicial)

    # Exibe o resultado
    print(f"O salário atual do funcionário é: R$ {salario_atual:.2f}")