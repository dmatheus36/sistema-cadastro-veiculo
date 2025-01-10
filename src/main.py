# main.py
from controllers import VeiculoController
from controllers.LoginController import LoginController
from models.database import initialize_db

if __name__ == "__main__":
    # Inicializa o banco de dados
    initialize_db()

    # Executa o login
    login_controller = LoginController()
    login_controller.iniciar_login()

    # Executa o controlador de veículos
    controller = VeiculoController()
    controller.executar()


