# Classe base para todos os veículos
class Veiculo:
    # Método construtor da classe Veiculo
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor              # Define a cor do veículo
        self.placa = placa          # Define a placa do veículo
        self.numero_rodas = numero_rodas  # Define o número de rodas do veículo

    # Método para simular a ação de ligar o motor do veículo
    def ligar_motor(self):
        print("Ligando o motor")

    # Método especial para representar o objeto como string
    def __str__(self):
        # Retorna uma string formatada com nome da classe e seus atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Classe Motocicleta herda de Veiculo
class Motocicleta(Veiculo):
    pass  # Não adiciona ou modifica funcionalidades de Veiculo

# Classe Carro herda de Veiculo
class Carro(Veiculo):
    pass  # Não adiciona ou modifica funcionalidades de Veiculo

# Classe Caminhao herda de Veiculo
class Caminhao(Veiculo):
    # Método construtor da classe Caminhao
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)  # Chama o construtor da classe pai
        self.carregado = carregado  # Define se o caminhão está carregado

    # Método para verificar se o caminhão está carregado
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

# Criação de objetos das subclasses
moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

# Impressão das representações em string dos objetos
print(moto)
print(carro)
print(caminhao)
