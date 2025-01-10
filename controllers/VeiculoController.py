# controllers/VeiculoController.py
from models.veiculoCRUD import VeiculoCRUD
from views.MainView import MainView
from models.carro import Carro
from models.moto import Moto
from models.caminhao import Caminhao
from models.JetSki import JetSki
from models.lancha import Lancha
from models.quadriciclo import Quadriciclo
import os

class VeiculoController:
    def __init__(self):
        self.crud = VeiculoCRUD()
        self.view = MainView()

    def executar(self):
        while True:
            self.view.exibir_menu()
            opcao = self.view.obter_opcao()

            if opcao == '1':
                self.cadastrar_veiculo()
            elif opcao == '2':
                self.atualizar_veiculo()
            elif opcao == '3':
                self.crud.listar_veiculos()
            elif opcao == '4':
                self.remover_veiculo()
            elif opcao == '0':
                print("Encerrando programa...")
                break
            else:
                self.view.mostrar_mensagem("Opção inválida!")

    def cadastrar_veiculo(self):
        tipo = input("Digite o tipo de veículo (carro / moto / quadriciclo / caminhao / jetski / lancha): ").lower()

        # Coletando os dados básicos
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        cor = input("Cor: ")
        ano = int(input("Ano: "))

        if tipo == 'carro':
            portas = int(input("Número de portas: "))
            capacidade = int(input("Capacidade de passageiros: "))
            hp = float(input("Cavalo de potência (HP): "))
            veiculo = Carro(None, marca, modelo, placa, cor, ano, portas, capacidade, hp)
        elif tipo == 'moto':
            cilindradas = int(input("Cilindradas: "))
            veiculo = Moto(None, marca, modelo, placa, cor, ano, cilindradas)

        elif tipo == 'caminhao':
            capacidade = int(input("Capacidade de passageiros: "))
            portas = int(input("Número de portas: "))
            carga = float(input("Capacidade máxima de carga (em toneladas): "))  # Certifique-se de que é float
            veiculo = Caminhao(None, marca, modelo, placa, cor, ano, capacidade, portas, carga)


        elif tipo == 'jetski':
            capacidade = int(input("Capacidade de passageiros: "))
            hp = float(input("Potência do motor (HP): "))
            veiculo = JetSki(None, marca, modelo, placa, cor, ano, capacidade, hp)
        elif tipo == 'lancha':
            capacidade = int(input("Capacidade de passageiros: "))
            hp = float(input("Potência do motor (HP): "))
            veiculo = Lancha(None, marca, modelo, placa, cor, ano, capacidade, hp)
        elif tipo == 'quadriciclo':
            capacidade = int(input("Capacidade de passageiros: "))
            hp = float(input("Potência do motor (HP): "))
            veiculo = Quadriciclo(None, marca, modelo, placa, cor, ano, capacidade, hp)
        else:
            self.view.mostrar_mensagem("Tipo de veículo inválido!")
            return

        self.crud.adicionar_veiculo(veiculo)
        self.view.mostrar_mensagem("Veículo cadastrado com sucesso!")



    def atualizar_veiculo(self):
        id = int(input("ID do veículo a ser atualizado: "))
        print("Atributo a atualizar (marca, modelo, placa, cor, ano, portas, capacidade, cargaMaxima, hp): ")
        atributo = input("Atributo a atualizar: ").lower()
        novo_valor = input("Novo valor: ")
        self.crud.atualizar_veiculo(id, **{atributo: novo_valor})

    def remover_veiculo(self):
        id = int(input("ID do veículo a ser removido: "))
        self.crud.remover_veiculo(id)
