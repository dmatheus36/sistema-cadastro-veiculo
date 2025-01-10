# admin.py

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_authenticated(self, input_username, input_password):
        return input_username == self.username and input_password == self.password

def login():
    admin = Admin(username="admin", password="senha123")

    print("Bem-vindo ao sistema!")
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if admin.is_authenticated(username, password):
        print("Login bem-sucedido!")
        return True
    else:
        print("Credenciais inválidas.")
        return False
