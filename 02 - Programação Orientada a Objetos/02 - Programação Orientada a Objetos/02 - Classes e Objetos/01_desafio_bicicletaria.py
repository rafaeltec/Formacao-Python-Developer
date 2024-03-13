# Definição da classe Bicicleta
class Bicicleta:
    # Método construtor, inicializa uma nova instância da classe Bicicleta
    def __init__(self, cor, modelo, ano, valor):
        # Atributos da classe são definidos aqui
        self.cor = cor        # Cor da bicicleta
        self.modelo = modelo  # Modelo da bicicleta
        self.ano = ano        # Ano da bicicleta
        self.valor = valor    # Valor da bicicleta

    # Método para simular o som de buzina da bicicleta
    def buzinar(self):
        print("Plim plim...")

    # Método para simular a ação de parar a bicicleta
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    # Método para simular a ação de correr com a bicicleta
    def correr(self):
        print("Vrummmmm...")

    # Método especial para representar o objeto como string
    def __str__(self):
        # Retorna uma string formatada com nome da classe e seus atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Criação de uma instância da classe Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
# Chamadas de métodos da instância b1
b1.buzinar()
b1.correr()
b1.parar()
# Impressão dos atributos da instância b1
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Criação de uma segunda instância da classe Bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189)
# Impressão da representação em string da instância b2, utilizando o método __str__
print(b2)
# Chamada do método correr da instância b2
b2.correr()


b3 = Bicicleta("azul", "caloi", 1980, 700)
print(b3)
b3.buzinar()
