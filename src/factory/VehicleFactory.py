# factory/VehicleFactory.py
from models.carro import Carro
from models.moto import Moto
from models.caminhao import Caminhao
from models.JetSki import JetSki
from models.lancha import Lancha
from models.quadriciclo import Quadriciclo

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, **kwargs):
        vehicle_classes = {
            "carro": Carro,
            "moto": Moto,
            "caminhao": Caminhao,
            "jetski": JetSki,
            "lancha": Lancha,
            "quadriciclo": Quadriciclo
        }

        if vehicle_type.lower() in vehicle_classes:
            return vehicle_classes[vehicle_type.lower()](**kwargs)
        else:
            raise ValueError(f"Tipo de veículo desconhecido: {vehicle_type}")
