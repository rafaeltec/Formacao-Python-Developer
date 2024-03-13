from abc import ABC, abstractmethod, abstractproperty

# Classe abstrata ControleRemoto
class ControleRemoto(ABC):
    # Método abstrato ligar
    @abstractmethod
    def ligar(self):
        pass

    # Método abstrato desligar
    @abstractmethod
    def desligar(self):
        pass

    # Propriedade abstrata marca
    @property
    @abstractproperty
    def marca(self):
        pass

# Classe ControleTV que herda de ControleRemoto
class ControleTV(ControleRemoto):
    # Implementação do método ligar
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    # Implementação do método desligar
    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    # Implementação da propriedade marca
    @property
    def marca(self):
        return "Philco"

# Classe ControleArCondicionado que herda de ControleRemoto
class ControleArCondicionado(ControleRemoto):
    # Implementação do método ligar
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    # Implementação do método desligar
    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    # Implementação da propriedade marca
    @property
    def marca(self):
        return "LG"

# Criação e uso de um objeto ControleTV
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)  # Imprime "Philco"

# Criação e uso de um objeto ControleArCondicionado
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)  # Imprime "LG"
