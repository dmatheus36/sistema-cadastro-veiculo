
import sqlite3
from sqlite3 import Error
import bcrypt

DATABASE_NAME = "login_system.db"

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

def initialize_db():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password BLOB NOT NULL
                );
            """)
            conn.commit()
        except Error as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            conn.close()

def add_user(username, password):
    hashed_password = hash_password(password)
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?);", (username, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"Erro: O nome de usuário '{username}' já existe.")
        except Error as e:
            print(f"Erro ao adicionar usuário: {e}")
        finally:
            conn.close()

def authenticate_user(username, password):
    conn = create_connection()
    is_authenticated = False
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = ?;", (username,))
            result = cursor.fetchone()
            if result and verify_password(password, result[0]):
                is_authenticated = True
        except Error as e:
            print(f"Erro ao autenticar usuário: {e}")
        finally:
            conn.close()
    return is_authenticated
