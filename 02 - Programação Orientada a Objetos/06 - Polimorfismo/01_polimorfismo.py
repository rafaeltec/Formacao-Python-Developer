# Classe base Passaro
class Passaro:
    # Método genérico voar
    def voar(self):
        print("Voando...")

# Classe Pardal herda de Passaro
class Pardal(Passaro):
    # Sobrescreve o método voar
    def voar(self):
        print("Pardal pode voar")

# Classe Avestruz herda de Passaro
class Avestruz(Passaro):
    # Sobrescreve o método voar
    def voar(self):
        print("Avestruz não pode voar")

# Classe Aviao herda de Passaro (não é uma boa prática)
class Aviao(Passaro):
    # Sobrescreve o método voar
    def voar(self):
        print("Avião está decolando...")

# Função que recebe um objeto e chama seu método voar
def plano_voo(obj):
    obj.voar()

# Testando a função com diferentes objetos
plano_voo(Pardal())      # Pardal pode voar
plano_voo(Avestruz())    # Avestruz não pode voar
plano_voo(Aviao())       # Avião está decolando...
