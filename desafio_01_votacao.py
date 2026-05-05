from os import system
system('cls')

candidatos = ['Ana', 'Bruno', 'Carlos']
votos = []

while True:
    voto = input('Candidatos: \n1 - Ana \n2 - Bruno \n3 - Carlos \nDigite o nome do candidato (Fim para encerrar): ').capitalize()
    if voto == 'Fim': break

    if voto in candidatos:
        votos.append(voto)
    else:
        print('Voto inválido. Tente novamente.\n')

        input('Pressione Enter para continuar...')

    if voto in candidatos:
       votos.count(voto)

print('\nResultado da votação:')
for voto in candidatos:
    print(f'{voto}: {votos.count(voto)} votos')

if votos:
    max_votos = max(votos.count(i) for i in candidatos)
    vencedores = [i for i in candidatos if votos.count(i) == max_votos]
    if len(vencedores) == 1:
        print(f'O vencedor é: {vencedores[0]}')
    else:
        print('Houve um empate entre os candidatos.')

print('\n\n')