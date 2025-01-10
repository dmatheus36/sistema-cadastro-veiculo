
from views.LoginView import LoginView
from models.database import authenticate_user

class LoginController:
    def __init__(self):
        self.view = LoginView()

    def iniciar_login(self):
        while True:
            username, password = self.view.exibir_tela_login()
            if authenticate_user(username, password):
                self.view.mostrar_mensagem("Login realizado com sucesso!")
                break
            else:
                self.view.mostrar_mensagem("Credenciais inválidas. Tente novamente.")
