# models/quadriciclo.py
class Quadriciclo:
    def __init__(self, id, marca, modelo, placa, cor, ano, capacidade, hp):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.ano = ano
        self.capacidade = capacidade
        self.hp = hp

    def __str__(self):
        return f"Quadriciclo [ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Placa: {self.placa}, Cor: {self.cor}, Ano: {self.ano}, Capacidade: {self.capacidade}, HP: {self.hp}]"
