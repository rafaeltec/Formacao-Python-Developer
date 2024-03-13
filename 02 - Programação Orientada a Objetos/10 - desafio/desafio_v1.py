from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

# Classe Cliente representando um cliente geral
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco  # Endereço do cliente
        self.contas = []          # Lista de contas associadas ao cliente

    def realizar_transacao(self, conta, transacao):
        # Executa uma transação em uma conta específica
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Adiciona uma conta à lista de contas do cliente
        self.contas.append(conta)

# Classe PessoaFisica, herda de Cliente, representa uma pessoa física
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Chama o construtor da classe base
        # Atributos específicos da pessoa física
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Classe Conta representando uma conta bancária genérica
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0             # Saldo inicial da conta
        self._numero = numero       # Número da conta
        self._agencia = "0001"      # Agência padrão
        self._cliente = cliente     # Cliente titular da conta
        self._historico = Historico()  # Histórico de transações da conta

    # Método de classe para criar uma nova conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Propriedades para acessar os atributos privados
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! Saldo insuficiente ou valor inválido. @@@")

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

# Classe ContaCorrente, herda de Conta, representa uma conta corrente
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Chama o construtor da classe base
        self.limite = limite                # Limite para saque
        self.limite_saques = limite_saques  # Limite de quantidade de saques

    # Sobrescreve o método sacar da classe base
    def sacar(self, valor):
        if valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        # Verifica o número de saques realizados
        elif len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]) >= self.limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    # Método especial para representar o objeto como string
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# Classe Historico representando o histórico de transações de uma conta
class Historico:
    def __init__(self):
        self._transacoes = []  # Lista para armazenar as transações

    # Propriedade para acessar as transações
    @property
    def transacoes(self):
        return self._transacoes

    # Método para adicionar uma transação ao histórico
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Tipo da transação
                "valor": transacao.valor,              # Valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),  # Data e hora da transação
            }
        )

# Classe abstrata Transacao para representar transações bancárias
class Transacao(ABC):
    # Propriedade abstrata valor
    @property
    @abstractproperty
    def valor(self):
        pass

    # Método abstrato para registrar a transação
    @abstractclassmethod
    def registrar(self, conta):
        pass

# Classe Saque, herda de Transacao, representa um saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Valor do saque

    # Propriedade para acessar o valor do saque
    @property
    def valor(self):
        return self._valor

    # Método para registrar o saque na conta
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

# Classe Deposito, herda de Transacao, representa um depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Valor do depósito

    # Propriedade para acessar o valor do depósito
    @property
    def valor(self):
        return self._valor

    # Método para registrar o depósito na conta
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
