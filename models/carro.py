class Carro:
    def __init__(self, id, marca, modelo, placa, cor, ano, portas,capacidade,hp):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.ano = ano
        self.portas = portas
        self.capacidade = capacidade
        self.hp = hp
    def __str__(self):
        return f"Carro [ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Placa: {self.placa}, Cor: {self.cor} Ano: {self.ano}, Portas: {self.portas}, Capaciade: {self.capacidade}, Hp: {self.hp}]"
