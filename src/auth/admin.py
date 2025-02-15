import hashlib
import sqlite3

def criar_tabela_usuario():
    """Cria a tabela de usuário no banco de dados, se não existir."""
    conn = sqlite3.connect('veiculos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT NOT NULL UNIQUE,
                        senha TEXT NOT NULL,
                        data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')
    conn.commit()
    conn.close()

def cadastrar_usuario():
    """Função para cadastrar um novo usuário."""
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    # Criptografar a senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    conn = sqlite3.connect('veiculos.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO usuario (usuario, senha)
                          VALUES (?, ?)''', (usuario, senha_hash))
        conn.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Nome de usuário já cadastrado.")
    
    conn.close()

def login(usuario, senha):
    """Função para fazer o login verificando o nome de usuário e senha."""
    conn = sqlite3.connect('veiculos.db')
    cursor = conn.cursor()

    # Criptografar a senha fornecida para comparação
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    cursor.execute('''SELECT * FROM usuario WHERE usuario = ? AND senha = ?''', (usuario, senha_hash))
    usuario_logado = cursor.fetchone()

    conn.close()

    if usuario_logado:
        return True  # Usuário encontrado, login bem-sucedido
    else:
        return False  # Credenciais inválidas

def deletar_usuario():
    """Função para deletar um usuário do banco de dados."""
    usuario = input("Digite o nome de usuário que deseja deletar: ")

    conn = sqlite3.connect('veiculos.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM usuario WHERE usuario = ?''', (usuario,))
    usuario_existente = cursor.fetchone()

    if usuario_existente:
        cursor.execute('''DELETE FROM usuario WHERE usuario = ?''', (usuario,))
        conn.commit()
        print(f"Usuário '{usuario}' deletado com sucesso!")
    else:
        print(f"Erro: Usuário '{usuario}' não encontrado.")

    conn.close()
