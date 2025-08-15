def exibir_cardapio():
    cardapio = {
        100: ('Cachorro Quente', 1.20),
        101: ('Bauru Simples', 1.30),
        102: ('Bauru com ovo', 1.50),
        103: ('Hambúrguer', 1.20),
        104: ('Cheeseburguer', 1.30),
        105: ('Refrigerante', 1.00),
    }

    print("Cardápio da Lanchonete:")
    print("-" * 30)
    for codigo, (especificacao, preco) in cardapio.items():
        print(f"{especificacao} / Código: {codigo} / Preço: R$ {preco:.2f}")
    print("-" * 30)

def fazer_pedido():
    total = 0
    while True:
        codigo = int(input("Digite o código do item que deseja pedir (ou 0 para finalizar): "))
        
        if codigo == 0:
            break
            
        if codigo not in range(100, 106):
            print("Código inválido! Tente novamente.")
            continue

        cardapio = {
            100: ('Cachorro Quente', 1.20),
            101: ('Bauru Simples', 1.30),
            102: ('Bauru com ovo', 1.50),
            103: ('Hambúrguer', 1.20),
            104: ('Cheeseburguer', 1.30),
            105: ('Refrigerante', 1.00),
        }

        especificacao, preco = cardapio[codigo]
        total += preco
        print(f"Você adicionou {especificacao} ao seu pedido. Preço: R$ {preco:.2f}")

    print(f"Total do pedido: R$ {total:.2f}")

def main():
    exibir_cardapio()
    fazer_pedido()