# Faça um programa que leia 5 números e informe o maior número.

maior =float('-inf')
menor =float('inf')
for i in range(5):
    n=int(input(f'digite o {i+1} numero: '))
    if maior < n:
        maior = n
    if menor > n:
        menor=n
print(f' O  maior numero digitado foi {maior}')
print(f' O  menor numero digitado foi {menor}')