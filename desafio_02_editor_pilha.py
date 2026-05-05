from os import system
system('cls')

opcoes = ['Digitar palavra', 'Desfazer última palavra', 'Mostrar texto', 'Sair']
palavras = []

while True:
    print('\nEDITOR DE TEXTO')
    for i, opcao in enumerate(opcoes, 1):
        print(f'[{i}] - {opcao}')

    escolha = input('Escolha uma opção: ')
    
    if escolha == '1':
        palavra = input('Digite uma palavra: ')
        palavras.append(palavra)

    elif escolha == '2':
        if palavras:
            palavras.pop()
            print('Última palavra desfeita.')
        else:
            print('Nenhuma palavra para desfazer.')
    elif escolha == '3':
        print('Texto atual:', ' '.join(palavras))
    elif escolha == '4': break
    else:
        print('Opção inválida. Tente novamente.')

    
print('\n\n')