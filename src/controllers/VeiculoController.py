# controllers/VeiculoController.py
from models.veiculoCRUD import VeiculoCRUD
from views.MainView import MainView
from factory.VehicleFactory import VehicleFactory

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

        dados_veiculo = {"id": None, "marca": marca, "modelo": modelo, "placa": placa, "cor": cor, "ano": ano}

        if tipo == 'carro':
            dados_veiculo.update({
                "portas": int(input("Número de portas: ")),
                "capacidade": int(input("Capacidade de passageiros: ")),
                "hp": float(input("Cavalo de potência (HP): "))
            })
        elif tipo == 'moto':
            dados_veiculo["cilindradas"] = int(input("Cilindradas: "))
        elif tipo == 'caminhao':
            dados_veiculo.update({
                "capacidade": int(input("Capacidade de passageiros: ")),
                "portas": int(input("Número de portas: ")),
                "cargaMaxima": float(input("Capacidade máxima de carga (em toneladas): "))
            })
        elif tipo in ['jetski', 'lancha', 'quadriciclo']:
            dados_veiculo.update({
                "capacidade": int(input("Capacidade de passageiros: ")),
                "hp": float(input("Potência do motor (HP): "))
            })
        else:
            self.view.mostrar_mensagem("Tipo de veículo inválido!")
            return

        veiculo = VehicleFactory.create_vehicle(tipo, **dados_veiculo)
        self.crud.adicionar_veiculo(veiculo)
        self.view.mostrar_mensagem("Veículo cadastrado com sucesso!")

    def atualizar_veiculo(self):
        id = int(input("ID do veículo a ser atualizado: "))
        atributo = input("Atributo a atualizar: ").lower()
        novo_valor = input(f"Novo valor para {atributo}: ")

        if atributo in ['ano', 'portas', 'capacidade', 'cargaMaxima', 'hp']:
            try:
                novo_valor = int(novo_valor) if atributo in ['ano', 'portas', 'capacidade'] else float(novo_valor)
            except ValueError:
                self.view.mostrar_mensagem("Erro: Valor inválido para o atributo.")
                return

        self.crud.atualizar_veiculo(id, **{atributo: novo_valor})
        self.view.mostrar_mensagem(f"Veículo {atributo} atualizado com sucesso!")

    def remover_veiculo(self):
        id = int(input("ID do veículo a ser removido: "))
        self.crud.remover_veiculo(id)
        self.view.mostrar_mensagem(f"Veículo com ID {id} removido com sucesso!")
