def calcular_fatorial():
    numero = int(input("Digite um número inteiro: "))
    
    if numero < 0:
        print("Fatorial não é definido para números negativos.")
        return
    
    fatorial = 1
    termos = []
    
    for i in range(numero, 0, -1):
        fatorial *= i
        termos.append(str(i))
    
    termos_formatados = ' . '.join(termos)
    
    print(f"\nFatorial de: {numero}")
    print(f"{numero}! = {termos_formatados} = {fatorial}")

calcular_fatorial()