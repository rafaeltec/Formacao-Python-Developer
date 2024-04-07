# Definição da classe Cachorro
class Cachorro:
    # Método de inicialização
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        # Definindo atributos da instância
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Método de finalização
    def __del__(self):
        print("Removendo a instância da classe.")

    # Método que permite ao cachorro "falar"
    def falar(self):
        print("auau")

# Definição da função criar_cachorro
def criar_cachorro():
    # Criando uma instância da classe Cachorro
    c = Cachorro("Zeus", "Branco e preto", False)
    # Imprimindo o nome do cachorro
    print(c.nome)

# Criando uma instância da classe Cachorro
c = Cachorro("Chappie", "amarelo")
# Cachorro "fala"
c.falar()



# Imprime na tela
print(c)

# Deleta a instância c do cachorro
#del c

# Imprime na tela
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()  # Esta linha está comentada, portanto, não será executada
