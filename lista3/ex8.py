# Faça um programa que leia 5 números e informe a soma e a média dos números.

media= 0
soma=0
for i in range(5):
    n = int(input(f'digite o {i+1} numero'))
    soma = soma + n
    media = soma /5 
    print(f'a soma é : {soma} e a media  { media}')