# Classe Conta representando uma conta bancária
class Conta:
    # Método construtor da classe Conta
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo        # Saldo inicial da conta, privado (_)
        self.nro_agencia = nro_agencia  # Número da agência da conta

    # Método para depositar um valor na conta
    def depositar(self, valor):
        # Aqui poderiam ser adicionadas verificações ou condições
        self._saldo += valor  # Adiciona o valor ao saldo

    # Método para sacar um valor da conta
    def sacar(self, valor):
        # Aqui poderiam ser adicionadas verificações ou condições
        self._saldo -= valor  # Subtrai o valor do saldo

    # Método para mostrar o saldo atual da conta
    def mostrar_saldo(self):
        # Retorna o saldo
        return self._saldo

# Criação de um objeto da classe Conta
conta = Conta("0001", 100)
# Depósito de 100 na conta
conta.depositar(100)
# Impressão do número da agência
print(conta.nro_agencia)
# Impressão do saldo atual da conta
print(conta.mostrar_saldo())
