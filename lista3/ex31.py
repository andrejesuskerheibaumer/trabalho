def caixa_registradora():
    while True:
        total_compra = 0.0
        produto_numero = 1
        
        print("Lojas Tabajara")
        
        while True:
            preco_produto = float(input(f"Produto {produto_numero}: R$ "))
            if preco_produto == 0:
                break
            total_compra += preco_produto
            produto_numero += 1
            
        print(f"Total: R$ {total_compra:.2f}")
        
        dinheiro_cliente = float(input("Dinheiro: R$ "))
        troco = dinheiro_cliente - total_compra
        print(f"Troco: R$ {troco:.2f}")
        
        continuar = input("Registrar outra compra? (s/n): ").lower()
        if continuar != 's':
            break

caixa_registradora()