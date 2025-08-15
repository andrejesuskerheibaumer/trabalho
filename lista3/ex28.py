def calcular_investimento_cds():
    quantidade_cds = int(input("Digite a quantidade de CDs na coleção: "))
    total_investido = 0.0

    for i in range(quantidade_cds):
        valor_cd = float(input(f"Digite o valor do CD {i + 1}: "))
        total_investido += valor_cd

    if quantidade_cds > 0:
        media_gasto = total_investido / quantidade_cds
        print(f"\nValor total investido na coleção: R$ {total_investido:.2f}")
        print(f"Valor médio gasto por CD: R$ {media_gasto:.2f}")
    else:
        print("Nenhum CD foi registrado.")

calcular_investimento_cds()