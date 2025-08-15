def obter_gabarito():
    gabarito = {}
    print("Digite o gabarito da prova:")
    for i in range(1, 11):
        resposta = input(f"Questão {i}: ").strip().upper()
        gabarito[i] = resposta
    return gabarito

def verificar_respostas(gabarito):
    acertos = 0
    for i in range(1, 11):
        resposta = input(f"Resposta da questão {i}: ").strip().upper()
        if resposta == gabarito[i]:
            acertos += 1
    return acertos

def main():
    gabarito = obter_gabarito()
    total_alunos = 0
    notas = []
    
    while True:
        total_alunos += 1
        acertos = verificar_respostas(gabarito)
        notas.append(acertos)
        print(f"Total de acertos: {acertos}")

        continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").strip().upper()
        if continuar != 'S':
            break
    
    if notas:
        maior_acerto = max(notas)
        menor_acerto = min(notas)
        media_notas = sum(notas) / len(notas)
        
        print(f"\nMaior acerto: {maior_acerto}")
        print(f"Menor acerto: {menor_acerto}")
        print(f"Total de alunos: {total_alunos}")
        print(f"Média das notas da turma: {media_notas:.2f}")
    else:
        print("Nenhum aluno foi registrado.")
