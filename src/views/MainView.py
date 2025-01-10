# views/MainView.py
class MainView:
    def exibir_menu(self):
        print("==========MENU================================")
        print("1 - CADASTRAR VEÍCULO")
        print("2 - ALTERAR DADOS DO VEÍCULO")
        print("3 - LISTAR VEÍCULOS")
        print("4 - DELETAR VEÍCULO")
        print("0 - SAIR")
        print("=============================================")

    def obter_opcao(self):
        return input("Digite o número da opção: ")

    def obter_dados_veiculo(self, tipo):
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        cor = input("Cor: ")
        ano = int(input("Ano: "))

        if tipo == 'carro':
            portas = int(input("Número de portas: "))
            capacidade = int(input("Capacidade do carro (em número de passageiros): "))
            hp = float(input("Cavalo de potência (HP): "))
            return marca, modelo, placa, cor, ano, portas, capacidade, hp
        elif tipo == 'moto':
            cilindradas = int(input("Cilindradas: "))
            return marca, modelo, placa, cor, ano, cilindradas
        # Similar para outros tipos de veículos...

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
