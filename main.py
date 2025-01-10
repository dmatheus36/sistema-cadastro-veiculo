# main.py
from controllers import VeiculoController
from auth.admin import login  # Corrigindo o caminho
  # Importando o sistema de login

if __name__ == "__main__":
    if login():  # Chama a função de login antes de executar o código principal
        controller = VeiculoController()
        controller.executar()
    else:
        print("Acesso negado. O código não será executado.")
