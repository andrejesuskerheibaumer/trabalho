def main():
    # Solicita o valor da dívida ao usuário
    valor_divida = float(input("Digite o valor da dívida: R$ "))

    # Lista de parcelas e suas respectivas taxas de juros
    parcelas = [1, 3, 6, 9, 12]
    juros = [0, 10, 15, 20, 25]

    print("\nValor da Dívida - Valor dos Juros - Quantidade de Parcelas - Valor da Parcela")

    # Calcula e exibe os resultados
    for i in range(len(parcelas)):
        quantidade_parcelas = parcelas[i]
        taxa_juros = juros[i]

        # Calcula o valor dos juros e o valor total da dívida
        valor_juros = (taxa_juros / 100) * valor_divida
        valor_total = valor_divida + valor_juros

        # Calcula o valor da parcela
        valor_parcela = valor_total / quantidade_parcelas

        # Exibe os resultados formatados
        print(f"R$ {valor_total:.2f} - R$ {valor_juros:.2f} - {quantidade_parcelas} - R$ {valor_parcela:.2f}")