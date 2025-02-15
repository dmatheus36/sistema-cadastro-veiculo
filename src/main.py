# main.py
from auth.admin import login, cadastrar_usuario, criar_tabela_usuario, deletar_usuario
from controllers.VeiculoController import VeiculoController




def menu():

    """Exibe as opções de login, cadastro e exclusão de usuários."""
    while True:
        print("\nEscolha uma opção:")
        print("1 - Logar")
        print("2 - Cadastrar")
        print("3 - Deletar Usuário")
        print("0 - Sair")
        
        opcao = input("Digite sua opção: ")

        if opcao == '1':
            usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            if login(usuario, senha):
                print("Login bem-sucedido!")
                controller = VeiculoController()
                controller.executar()
            else:
                print("Erro: Credenciais inválidas.")
        elif opcao == '2':
            cadastrar_usuario()
        elif opcao == '3':
            deletar_usuario()  # Chamando a função para deletar usuário
        elif opcao == '0':
            print("Saindo do sistema...")
            break  # Encerra o loop e sai do programa
        else:
            print("Opção inválida. Tente novamente.")

def main():
    """Função principal que chama o menu e inicializa o sistema."""
    criar_tabela_usuario()  # Criar a tabela de usuário se não existir
    menu()  # Exibir o menu

# Chamar a função principal
if __name__ == "__main__":
    main()