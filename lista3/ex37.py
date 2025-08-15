def main():
    # Inicializa variáveis
    clientes = []
    
    while True:
        # Solicita os dados do cliente
        codigo = int(input("Digite o código do cliente (ou 0 para encerrar): "))
        
        # Encerra a coleta de dados se o código for 0
        if codigo == 0:
            break
        
        altura = float(input("Digite a altura do cliente (em metros): "))
        peso = float(input("Digite o peso do cliente (em kg): "))
        
        # Adiciona os dados do cliente à lista
        clientes.append((codigo, altura, peso))
    
    # Verifica se há clientes cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    # Inicializa variáveis para encontrar o mais alto, mais baixo, mais gordo e mais magro
    mais_alto = max(clientes, key=lambda x: x[1])
    mais_baixo = min(clientes, key=lambda x: x[1])
    mais_gordo = max(clientes, key=lambda x: x[2])
    mais_mago = min(clientes, key=lambda x: x[2])
    
    # Calcula a média das alturas e pesos
    media_altura = sum(cliente[1] for cliente in clientes) / len(clientes)
    media_peso = sum(cliente[2] for cliente in clientes) / len(clientes)

    # Exibe os resultados
    print("\nResultados:")
    print(f"Cliente mais alto: Código {mais_alto[0]}, Altura {mais_alto[1]} m, Peso {mais_alto[2]} kg")
    print(f"Cliente mais baixo: Código {mais_baixo[0]}, Altura {mais_baixo[1]} m, Peso {mais_baixo[2]} kg")
    print(f"Cliente mais gordo: Código {mais_gordo[0]}, Altura {mais_gordo[1]} m, Peso {mais_gordo[2]} kg")
    print(f"Cliente mais magro: Código {mais_mago[0]}, Altura {mais_mago[1]} m, Peso {mais_mago[2]} kg")
    print(f"Média das alturas: {media_altura:.2f} m")
    print(f"Média dos pesos: {media_peso:.2f} kg")

