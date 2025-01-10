class JetSki:
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
        return (f"JetSki [ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Placa: {self.placa}, Cor: {self.cor}, Ano: {self.ano}, "
                f"Capacidade: {self.capacidade}, HP: {self.hp}]")
