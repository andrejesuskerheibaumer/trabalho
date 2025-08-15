def main():
    cidades = []  # Lista para armazenar dados das cidades

    for i in range(5):  # Para 5 cidades
        print(f"\nDados da cidade {i + 1}:")
        codigo = input("Digite o código da cidade: ")
        num_veiculos = int(input("Digite o número de veículos de passeio (em 1999): "))
        num_acidentes = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))
        cidades.append((codigo, num_veiculos, num_acidentes))

    # Inicializa variáveis para calcular índices
    maior_acidente = cidades[0]
    menor_acidente = cidades[0]
    total_veiculos = 0
    total_acidentes_menos_2000 = 0
    contador_menos_2000 = 0

    # Processa os dados coletados
    for cidade in cidades:
        codigo, num_veiculos, num_acidentes = cidade
        
        # Calcular total de veículos
        total_veiculos += num_veiculos
        
        # Determine maior e menor índice de acidentes
        if num_acidentes > maior_acidente[2]:
            maior_acidente = cidade
        if num_acidentes < menor_acidente[2]:
            menor_acidente = cidade

        # Calcular média de acidentes para cidades com menos de 2000 veículos
        if num_veiculos < 2000:
            total_acidentes_menos_2000 += num_acidentes
            contador_menos_2000 += 1

    # Cálculo das médias
    media_veiculos = total_veiculos / 5
    media_acidentes_menos_2000 = (total_acidentes_menos_2000 / contador_menos_2000) if contador_menos_2000 > 0 else 0

    # Exibe os resultados
    print(f"\nCidade com maior índice de acidentes: Código {maior_acidente[0]}, Acidentes {maior_acidente[2]}")
    print(f"Cidade com menor índice de acidentes: Código {menor_acidente[0]}, Acidentes {menor_acidente[2]}")
    print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")
    print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menos_2000:.2f}")