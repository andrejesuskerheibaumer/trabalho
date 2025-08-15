def calcular_serie(n):
    soma = 0.0
    termos = []
    
    for i in range(1, n + 1):
        denominador = 2 * i - 1
        termo = i / denominador
        termos.append(termo)
        soma += termo
        
    return termos, soma

def main():
    n = int(input("Digite o número de termos da série (n): "))
    termos, soma = calcular_serie(n)
    
    print("Os termos da série são:")
    for termo in termos:
        print(f"{termo:.6f}")
    
    print(f"\nA soma da série é: {soma:.6f}")
    