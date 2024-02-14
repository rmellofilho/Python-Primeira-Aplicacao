import os


restaurantes = []


def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app():
    os.system("cls")
    # os.system("clear") no mac os
    print("Finalizando o app\n")


def opcao_invalida():
    print('Opção inválida!\n')
    print('Digite uma tecla para voltar ao menu principal')
    main()


def cadastrar_novo_restaurante():
    os.system("cls")
    print('Cadastro de novos restaurantes')
    nome_do_restaurante = (input("Digine o nome do restaurante que deseja cadastrar: "))
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f"Você escolheu a opção', {opcao_escolhida}")

        if(opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif(opcao_escolhida == 2):
            print("Listar restaurante")
        elif(opcao_escolhida == 3):
            print("Ativar restaurante")
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