from os import system
system('cls')

fila = []
opcoes = ['Retirar senha', 'Chamar próximo aluno', 'Mostrar fila', 'Sair']

while True:
    print('\nSECRETARIA ACADÊMICA')
    for i, opcao in enumerate(opcoes, 1):
        print(f'[{i}] - {opcao}')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        nome = input('Digite o nome do cliente: ').capitalize()
        fila.append(nome)
        print(f'{nome} entrou na fila de atendimento.')
    elif escolha == '2':
        if fila:
            atendido = fila.pop(0)
            print('Chamado o aluno:', atendido)
        else:
            print('Nenhum aluno na fila.')
    elif escolha == '3':
        print('Fila atual:')
        if not fila:
            print('A fila está vazia.')
        for i, nome in enumerate(fila, 1):
            print(f'{i}º - {nome}')
    elif escolha == '4':
        break
    else:
        print('Opção inválida. Tente novamente.')

print('\n\n')