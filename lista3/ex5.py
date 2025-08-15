#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

popa= float(input('digite a popula de A'))
taxaa=float(input('digite a taxa de crescimento de A'))
taxaa= taxaa/ 100
print(taxaa)

popb= float(input('digite a popula de B'))
taxab=float(input('digite a taxa de crescimento de B'))
taxab=taxab/ 100
print(taxab)
ano = 0

while popa <= popb:
    popa += popa * taxaa
    popb += popb * taxab
    ano += 1
    print(f'ano {ano} : pop a = {popa}, pop b = {popb}')
print(f'A população A ultrapassou ou igualou B em {ano}')