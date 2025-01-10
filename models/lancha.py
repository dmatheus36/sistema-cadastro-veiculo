class Lancha:
    def __init__(self, id, marca, modelo, placa, cor, ano, capacidade, hp):
        """
        Classe Lancha para representar uma lancha.

        Args:
            id (int): Identificador único da lancha.
            marca (str): Marca da lancha.
            modelo (str): Modelo da lancha.
            placa (str): Placa de identificação da lancha.
            cor (str): Cor da lancha.
            ano (int): Ano de fabricação.
            capacidade (int): Capacidade de passageiros.
            hp (float): Potência do motor em cavalos (HP).
        """
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.ano = ano
        self.capacidade = capacidade
        self.hp = hp

    def __str__(self):
        return (f"Lancha [ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Placa: {self.placa}, Cor: {self.cor}, Ano: {self.ano}, "
                f"Capacidade: {self.capacidade}, HP: {self.hp}]")
