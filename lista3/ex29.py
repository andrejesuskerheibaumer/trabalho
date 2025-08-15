def gerar_tabela_precos():
    print("Lojas Quase Dois - Tabela de preços")
    print("-" * 30)
    
    for i in range(1, 51):
        preco = 1.99 * i
        print(f"{i} - R$ {preco:.2f}")

gerar_tabela_precos()