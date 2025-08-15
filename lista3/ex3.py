"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    nome = input('digite o nome: ')

    while len(nome)<3:
        print(f'digiteou um, nome maior que 3 =>{nome}')

    idade =int(input('digite a idade: ')) 
    while idade <0 or idade > 150:
       print(f'digite a idade {idade}')
    salario= float(input('salario: '))
    while salario <0:
        print(f'digite o salario{salario}')
    sexo= input('digite seu sexo [f/m]: ')
    sexo = sexo.lower()
    while sexo != 'f' and sexo != 'm':
        print('sexo invalido')
        sexo= input('digite seu sexo [f/m]')
        sexo = sexo.lower()
    civil= input('digite seu estado civil [s/c/v/d]: ')
    civil=civil.lower()
    while civil != 's' and civil != 'c'and civil != 'v'and civil != 'd':
        print('estado civil invalido')
        civil= input('digite seu estado civil [s/c/v/d]')
        civil = civil.lower()


    break