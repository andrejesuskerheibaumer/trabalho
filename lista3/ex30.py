def gerar_tabela_precos_pao():
    preco_pao = float(input("Digite o preço do pão: R$ "))
    
    print("Panificadora Pão de Ontem - Tabela de preços")
    print("-" * 40)
    
    for i in range(1, 51):
        preco_total = preco_pao * i
        print(f"{i} - R$ {preco_total:.2f}")

gerar_tabela_precos_pao()