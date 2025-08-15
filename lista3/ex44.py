def exibir_cardapio():
    cardapio = {
        100: ('Cachorro Quente', 1.20),
        101: ('Bauru Simples', 1.30),
        102: ('Bauru com ovo', 1.50),
        103: ('Hambúrguer', 1.20),
        104: ('Cheeseburguer', 1.30),
        105: ('Refrigerante', 1.00),
    }

    print("\nCardápio da Lanchonete:")
    print("-" * 30)
    for codigo, (especificacao, preco) in cardapio.items():
        print(f"{codigo} - {especificacao}: R$ {preco:.2f}")
    print("-" * 30)

def fazer_pedido():
    cardapio = {
        100: ('Cachorro Quente', 1.20),
        101: ('Bauru Simples', 1.30),
        102: ('Bauru com ovo', 1.50),
        103: ('Hambúrguer', 1.20),
        104: ('Cheeseburguer', 1.30),
        105: ('Refrigerante', 1.00),
    }

    total_geral = 0
    print("\nRealize seu pedido")
    while True:
        codigo = int(input("Digite o código do item (ou 0 para finalizar): "))
        
        if codigo == 0:
            break
            
        if codigo not in cardapio:
            print("Código inválido! Tente novamente.")
            continue

        quantidade = int(input(f"Quantia de {cardapio[codigo][0]}: "))
        if quantidade < 0:
            print("Quantidade inválida! Deve ser um número positivo.")
            continue

        preco = cardapio[codigo][1]
        valor_item = preco * quantidade
        total_geral += valor_item
        print(f"{quantidade} x {cardapio[codigo][0]}: R$ {valor_item:.2f}")

    print(f"Total do pedido: R$ {total_geral:.2f}")

def contabilizar_votos():
    votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    candidatos = {
        1: "José",
        2: "João",
        3: "Maria",
        4: "Ana"
    }

    print("\nVotação:")
    print("1 - José")
    print("2 - João")
    print("3 - Maria")
    print("4 - Ana")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    print("0 - Encerrar votação")

    while True:
        voto = int(input("Vote (1-6): "))
        
        if voto == 0:
            break
            
        if voto in votos:
            votos[voto] += 1
        else:
            print("Voto inválido! Tente novamente.")

    total_votos = sum(votos.values())
    
    print("\nResultados da Eleição:")
    print("-" * 30)
    for candidato in range(1, 5):
        print(f"Total de votos para {candidatos[candidato]}: {votos[candidato]}")
    
    print(f"Total de votos nulos: {votos[5]}")
    print(f"Total de votos em branco: {votos[6]}")

    if total_votos > 0:
        perc_nulos = (votos[5] / total_votos) * 100
        perc_brancos = (votos[6] / total_votos) * 100
        print(f"Percentagem de votos nulos: {perc_nulos:.2f}%")
        print(f"Percentagem de votos em branco: {perc_brancos:.2f}%")
    else:
        print("Nenhum voto registrado.")

def main():
    fazer_pedido()
    contabilizar_votos()