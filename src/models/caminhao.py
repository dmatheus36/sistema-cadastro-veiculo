# models/caminhao.py
class Caminhao:
    def __init__(self, id, marca, modelo, placa, cor, ano, capacidade, portas, cargaMaxima):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.ano = ano
        self.portas = portas
        self.capacidade = capacidade
        self.cargaMaxima = cargaMaxima

    def __str__(self):
        return f"Caminhão [ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Placa: {self.placa}, Cor: {self.cor}, Ano: {self.ano}, Capacidade: {self.capacidade}, Portas: {self.portas}, Carga Máxima: {self.cargaMaxima}]"
