
class LoginView:
    def exibir_tela_login(self):
        print("=== Sistema de Login ===")
        username = input("Usuário: ")
        password = input("Senha: ")
        return username, password

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
