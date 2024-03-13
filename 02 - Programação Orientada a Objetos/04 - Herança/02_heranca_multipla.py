# Classe base Animal
class Animal:
    # Construtor da classe Animal
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas  # Número de patas do animal

    # Método especial para representar o objeto como string
    def __str__(self):
        # Retorna uma string formatada com o nome da classe e seus atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Classe Mamifero herda de Animal
class Mamifero(Animal):
    # Construtor da classe Mamifero
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo  # Cor do pelo do mamífero
        super().__init__(**kw)  # Passa os argumentos restantes para o construtor da classe base

# Classe Ave herda de Animal
class Ave(Animal):
    # Construtor da classe Ave
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico  # Cor do bico da ave
        super().__init__(**kw)  # Passa os argumentos restantes para o construtor da classe base

# Classe Gato herda de Mamifero
class Gato(Mamifero):
    pass  # Não adiciona ou modifica funcionalidades de Mamifero

# Classe Ornitorrinco herda de Mamifero e Ave
class Ornitorrinco(Mamifero, Ave):
    # Construtor da classe Ornitorrinco
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # Inicializa a classe usando os construtores das classes base
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

# Criação de um objeto Gato
gato = Gato(nro_patas=4, cor_pelo="Preto")
# Impressão da representação em string do objeto gato
print(gato)

# Criação de um objeto Ornitorrinco
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
# Impressão da representação em string do objeto ornitorrinco
print(ornitorrinco)
