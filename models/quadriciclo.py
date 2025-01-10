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

    def __repr__(self):
        return f"Quadriciclo({self.marca}, {self.modelo}, {self.placa}, {self.cor}, {self.ano}, {self.capacidade}, {self.hp})"
