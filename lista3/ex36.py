def main():
    # Solicita o número para a tabuada
    numero = int(input("Montar a tabuada de: "))
    
    # Solicita o valor inicial da tabuada
    inicio = int(input("Começar por: "))
    
    # Solicita o valor final da tabuada
    fim = int(input("Terminar em: "))

    # Verifica se o valor final é menor que o valor inicial
    if fim < inicio:
        print("Erro: o valor final não pode ser menor que o valor inicial.")
        return

    # Monta a tabuada
    print(f"\nVou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:\n")
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

