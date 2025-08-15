def calcular_media_idade():
    idades = []
    numero_de_pessoas = int(input("Quantas pessoas você deseja inserir a idade? "))
    
    for i in range(numero_de_pessoas):
        idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
        idades.append(idade)

    media_idade = sum(idades) / numero_de_pessoas
    print(f"A média de idade da turma é: {media_idade:.2f}")

    if media_idade >= 0 and media_idade <= 25:
        print("A turma é jovem.")
    elif media_idade > 25 and media_idade <= 60:
        print("A turma é adulta.")
    else:
        print("A turma é idosa.")

calcular_media_idade()
