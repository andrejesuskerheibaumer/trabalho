

soma=0
n1 = int(input('digite o primeiro numero'))
n2 = int(input('digite o segundo numero'))

for i in range(n1+1, n2):
    print(i)
    soma= soma + 1
print(f' A soma dos numeros digitando {soma}')