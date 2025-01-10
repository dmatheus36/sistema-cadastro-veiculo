class Moto:
    def __init__(self, id, marca, modelo, placa, cor, ano, cilindradas):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.ano = ano
        self.cilindradas = cilindradas

    def __str__(self):
        return f"Moto [ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Placa: {self.placa}, Cor: {self.cor}, Ano: {self.ano}, Cilindradas: {self.cilindradas}]"
