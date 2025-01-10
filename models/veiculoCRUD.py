# models/VeiculoCRUD.py
import sqlite3
import os
class VeiculoCRUD:
    def __init__(self):
        # Conexão com o banco de dados SQLite
        self.conn = sqlite3.connect("veiculos.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        # Criação da tabela se não existir
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS veiculos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            tipo TEXT,
                            marca TEXT,
                            modelo TEXT,
                            placa TEXT UNIQUE,
                            cor TEXT,
                            ano INTEGER,
                            portas INTEGER,
                            capacidade INTEGER,
                            cargaMaxima REAL,
                            cilindradas,
                            hp REAL)''')
        self.conn.commit()

    def adicionar_veiculo(self, veiculo):
        tipo = veiculo.__class__.__name__.lower()

        # Verificar se o veículo já existe com a mesma placa
        self.cursor.execute("SELECT id FROM veiculos WHERE placa = ?", (veiculo.placa,))
        if self.cursor.fetchone():
            print("\033[1;33mErro: Veículo já existe no banco de dados.\033[m")
            return

        # Dados do veículo para inserção (sem o 'id')
        dados_veiculo = {
            'tipo': tipo,
            'marca': veiculo.marca,
            'modelo': veiculo.modelo,
            'placa': veiculo.placa,
            'cor': veiculo.cor,
            'ano': veiculo.ano,
            'portas': getattr(veiculo, 'portas', None),
            'capacidade': getattr(veiculo, 'capacidade', None),
            'cargaMaxima': getattr(veiculo, 'cargaMaxima', None),
            'cilindradas': getattr(veiculo, 'cilindradas', None),
            'hp': getattr(veiculo, 'hp', None),
        }

        # Inserir o veículo sem especificar o 'id'
        self.cursor.execute('''INSERT INTO veiculos (tipo, marca, modelo, placa, cor, ano, portas, capacidade, cargaMaxima, cilindradas, hp)
                               VALUES (:tipo, :marca, :modelo, :placa, :cor, :ano, :portas, :capacidade, :cargaMaxima, :cilindradas, :hp)''', dados_veiculo)
        self.conn.commit()
        print(f"Veículo adicionado: {veiculo}")

    def listar_veiculos(self):
        
        self.cursor.execute("SELECT * FROM veiculos")
        veiculos = self.cursor.fetchall()
        if not veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print(f"\033[1;35m(ID, TIPO, MARCA, MODELO, PLACA, COR, ANO, PORTAS, CAPACIDADE Nº(PESSOAS), CARGAMAXIMA, CILINDRADAS, HP) \033[m")
            for v in veiculos:
                print(f"\033[1;32m{v}\033[m")

    def atualizar_veiculo(self, id, **novos_dados):
        set_clause = ', '.join([f"{k} = ?" for k in novos_dados])
        valores = list(novos_dados.values()) + [id]
        self.cursor.execute(f"UPDATE veiculos SET {set_clause} WHERE id = ?", valores)
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Veículo atualizado com sucesso.")
        else:
            print("Veículo não encontrado.")

    def remover_veiculo(self, id):
        self.cursor.execute("DELETE FROM veiculos WHERE id = ?", (id,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Veículo removido com sucesso.")
        else:
            print("Veículo não encontrado.")

    def __del__(self):
        self.cursor.close()
        self.conn.close()
