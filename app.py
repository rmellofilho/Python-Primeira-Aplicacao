import os


restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana ', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana ', 'ativo': False}]


def exibir_nome_do_programa():
    ''' Essa função é repsponsável por imprimir o nome do programa
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_opcoes():
    ''' Essa função é repsponsável por imprimir as opções da lista
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    ''' Essa função é repsponsável por encerrar o programa
    '''
    exibir_subtitulo('Finalizando o app\n')


def voltar_ao_menu_principal():
    ''' 
    Essa função é responsável por solicitar ao usuário que pressione uma tecla para voltar ao menu principal.
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()


def opcao_invalida():
    ''' 
    Essa função é responsável por imprimir uma mensagem de opção inválida e chamar a função voltar_ao_menu_principal() para o usuário tentar selecionar uma opção novamente.
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    ''' 
    Essa função é responsável por imprimir um subtitulo com um texto.
    
    Inputs:
        texto (str): O texto do subtitulo.
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    ''' Essa função é repsponsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input("Digine o nome do restaurante que deseja cadastrar: ")
    categoria = input(f'Digite o nome da categoria {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    ''' 
    Essa função é responsável por listar os restaurantes.
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    ''' 
    Essa função é responsável por alterar o estado de um restaurante (ativo/desativado).
    '''
    exibir_subtitulo("Alterando estado do restaurante")

    nome_restaurante = input('Digine o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucessso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    ''' 
    Essa função é responsável por permitir ao usuário escolher uma opção do menu.
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f"Você escolheu a opção', {opcao_escolhida}")

        if(opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif(opcao_escolhida == 2):
            listar_restaurantes()
        elif(opcao_escolhida == 3):
            alterar_estado_restaurante()
        elif(opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida() 


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()