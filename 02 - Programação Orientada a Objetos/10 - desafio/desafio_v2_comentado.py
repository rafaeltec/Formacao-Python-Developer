# Importa bibliotecas necessárias para o programa.
import textwrap  # Para formatar a saída de texto de forma organizada.
from abc import ABC, abstractclassmethod, abstractproperty  # Para criar classes abstratas.
from datetime import datetime  # Para trabalhar com datas e horas.

# Classe que representa um cliente do banco.
class Cliente:
    # Método construtor da classe Cliente.
    def __init__(self, endereco):
        # Armazena o endereço do cliente.
        self.endereco = endereco
        # Cria uma lista vazia para armazenar as contas do cliente.
        self.contas = [] 

    # Método para realizar uma transação em uma conta do cliente.
    def realizar_transacao(self, conta, transacao):
        # Chama o método 'registrar' da transação, passando a conta como argumento.
        transacao.registrar(conta)  

    # Método para adicionar uma conta à lista de contas do cliente.
    def adicionar_conta(self, conta):
        # Adiciona a conta à lista de contas do cliente.
        self.contas.append(conta)  

# Classe que representa uma pessoa física como cliente do banco, herdando de Cliente.
class PessoaFisica(Cliente):
    # Método construtor da classe PessoaFisica.
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Chama o construtor da classe pai (Cliente) para inicializar endereco e contas.
        super().__init__(endereco)  
        # Armazena o nome da pessoa física.
        self.nome = nome
        # Armazena a data de nascimento da pessoa física. 
        self.data_nascimento = data_nascimento 
        # Armazena o CPF da pessoa física.
        self.cpf = cpf  

# Classe que representa uma conta bancária.
class Conta:
    # Método construtor da classe Conta.
    def __init__(self, numero, cliente):
        # Inicializa o saldo da conta com 0.
        self._saldo = 0  
        # Armazena o número da conta.
        self._numero = numero 
        # Define a agência da conta (nesse caso, fixa em "0001").
        self._agencia = "0001"  
        # Armazena o cliente associado à conta.
        self._cliente = cliente  
        # Cria um objeto Historico para registrar as transações da conta.
        self._historico = Historico()  

    # Método de classe para criar uma nova conta.
    @classmethod
    def nova_conta(cls, cliente, numero):
        # Retorna uma nova instância da classe Conta com o cliente e número especificados.
        return cls(numero, cliente) 

    # Propriedade para acessar o saldo da conta.
    @property
    def saldo(self):
        # Retorna o valor do atributo _saldo.
        return self._saldo  

    # Propriedade para acessar o número da conta.
    @property
    def numero(self):
        # Retorna o valor do atributo _numero.
        return self._numero 

    # Propriedade para acessar a agência da conta.
    @property
    def agencia(self):
        # Retorna o valor do atributo _agencia.
        return self._agencia 

    # Propriedade para acessar o cliente associado à conta.
    @property
    def cliente(self):
        # Retorna o valor do atributo _cliente.
        return self._cliente 

    # Propriedade para acessar o histórico de transações da conta.
    @property
    def historico(self):
        # Retorna o valor do atributo _historico.
        return self._historico 

    # Método para sacar dinheiro da conta.
    def sacar(self, valor):
        # Verifica se o valor do saque é maior que o saldo da conta.
        if valor > self.saldo: 
            # Exibe mensagem de erro se o saldo for insuficiente.
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")  
        # Verifica se o valor do saque é positivo. 
        elif valor > 0:  
            # Subtrai o valor do saque do saldo da conta.
            self._saldo -= valor  
            # Exibe mensagem de sucesso.
            print("\n=== Saque realizado com sucesso! ===")  
            # Retorna True para indicar que a operação foi bem-sucedida.
            return True  
        else:
            # Exibe mensagem de erro se o valor do saque for inválido.
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  
            # Retorna False para indicar que a operação falhou. 
            return False 
           # Método para depositar dinheiro na conta.
    def depositar(self, valor):
        # Verifica se o valor do depósito é positivo.
        if valor > 0:  
            # Adiciona o valor do depósito ao saldo da conta.
            self._saldo += valor  
            # Exibe mensagem de sucesso. 
            print("\n=== Depósito realizado com sucesso! ===")  
            # Retorna True para indicar que a operação foi bem-sucedida.
        else:
            # Exibe mensagem de erro se o valor do depósito for inválido.
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  
            # Retorna False para indicar que a operação falhou. 
            return False  
        return True

# Classe que representa uma conta corrente, herdando de Conta.
class ContaCorrente(Conta):
    # Método construtor da classe ContaCorrente.
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Chama o construtor da classe pai (Conta) para inicializar os atributos básicos.
        super().__init__(numero, cliente)  
        # Define o limite de saque da conta corrente. 
        self._limite = limite  
        # Define o limite de número de saques diários da conta corrente.
        self._limite_saques = limite_saques  

    # Método para sacar dinheiro da conta corrente, considerando limites.
    def sacar(self, valor):
        # Obtém o número de saques realizados hoje.
        numero_saques = len([transacao for transacao in self.historico.transacoes 
                            if transacao["tipo"] == Saque.__name__]) 
        # Verifica se o valor do saque excede o limite.
        if valor > self._limite:  
            # Exibe mensagem de erro se o valor excede o limite.
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")  
        # Verifica se o número de saques excede o limite diário.
        elif numero_saques >= self._limite_saques:  
            # Exibe mensagem de erro se o número de saques excede o limite.
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@") 
        else:
            # Chama o método sacar da classe pai (Conta) se os limites forem respeitados. 
            return super().sacar(valor)  
        # Retorna False se a operação falhou devido aos limites.
        return False  

    # Método para representar a conta corrente como string.
    def __str__(self):
        # Retorna uma string formatada com informações da conta corrente.
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """ 

# Classe para armazenar e gerenciar o histórico de transações de uma conta.
class Historico:
    # Método construtor da classe Historico.
    def __init__(self):
        # Cria uma lista vazia para armazenar as transações.
        self._transacoes = []  

    # Propriedade para acessar a lista de transações.
    @property
    def transacoes(self):
        # Retorna a lista de transações.
        return self._transacoes 

    # Método para adicionar uma transação ao histórico. 
    def adicionar_transacao(self, transacao):
        # Adiciona um dicionário com informações da transação à lista de transações.
        self._transacoes.append({ 
            "tipo": transacao.__class__.__name__,  # Nome da classe da transação (Saque ou Deposito).
            "valor": transacao.valor,  # Valor da transação.
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),  # Data e hora da transação.
        })  
# Classe abstrata para representar transações bancárias.
class Transacao(ABC):
    # Propriedade abstrata para o valor da transação.
    @property
    @abstractproperty
    def valor(self):
        pass

    # Método abstrato para registrar a transação em uma conta.
    @abstractclassmethod
    def registrar(self, conta):
        pass

# Classe que representa uma transação de saque, herdando de Transacao.
class Saque(Transacao):
    # Método construtor da classe Saque.
    def __init__(self, valor):
        # Armazena o valor do saque.
        self._valor = valor  

    # Propriedade para acessar o valor do saque.
    @property
    def valor(self):
        # Retorna o valor do atributo _valor.
        return self._valor  

    # Método para registrar a transação de saque em uma conta. 
    def registrar(self, conta):
        # Tenta realizar o saque na conta.
        sucesso_transacao = conta.sacar(self.valor)  
        # Se o saque for bem-sucedido, adiciona a transação ao histórico da conta.
        if sucesso_transacao:  
            conta.historico.adicionar_transacao(self)  

# Classe que representa uma transação de depósito, herdando de Transacao.
class Deposito(Transacao):
    # Método construtor da classe Deposito.
    def __init__(self, valor):
        # Armazena o valor do depósito. 
        self._valor = valor  

    # Propriedade para acessar o valor do depósito.
    @property
    def valor(self):
        # Retorna o valor do atributo _valor.
        return self._valor  

    # Método para registrar a transação de depósito em uma conta.
    def registrar(self, conta):
        # Tenta realizar o depósito na conta.
        sucesso_transacao = conta.depositar(self.valor)  
        # Se o depósito for bem-sucedido, adiciona a transação ao histórico da conta. 
        if sucesso_transacao: 
            conta.historico.adicionar_transacao(self) 

# Função para exibir o menu de opções para o usuário.
def menu():
    # Define o texto do menu.
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    # Retorna a opção escolhida pelo usuário.
    return input(textwrap.dedent(menu))  

# Função para encontrar um cliente na lista de clientes pelo CPF.
def filtrar_cliente(cpf, clientes):
    # Filtra a lista de clientes pelo CPF.
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf] 
    # Retorna o primeiro cliente encontrado ou None se não encontrar nenhum.
    return clientes_filtrados[0] if clientes_filtrados else None  

# Função para recuperar a conta de um cliente (por enquanto, retorna a primeira conta).
def recuperar_conta_cliente(cliente):
    # Verifica se o cliente possui alguma conta.
    if not cliente.contas:  
        # Exibe mensagem de erro se o cliente não tiver contas.
        print("\n@@@ Cliente não possui conta! @@@")  
        # Retorna None se o cliente não tiver contas.
        return  
    # Retorna a primeira conta da lista de contas do cliente.
    return cliente.contas[0]  

# Função para realizar um depósito em uma conta.
def depositar(clientes):
    # Obtém o CPF do cliente.
    cpf = input("Informe o CPF do cliente: ")  
    # Encontra o cliente na lista de clientes pelo CPF.
    cliente = filtrar_cliente(cpf, clientes)  
    # Verifica se o cliente foi encontrado.
    if not cliente:  
        # Exibe mensagem de erro se o cliente não for encontrado.
        print("\n@@@ Cliente não encontrado! @@@")  
        # Retorna se o cliente não for encontrado.
        return  
    # Obtém o valor do depósito.
    valor = float(input("Informe o valor do depósito: "))  
    # Cria uma transação de depósito.
    transacao = Deposito(valor)  
    # Recupera a conta do cliente. 
    conta = recuperar_conta_cliente(cliente)  
    # Verifica se a conta foi recuperada.
    if not conta:  
        # Retorna se a conta não for recuperada. 
        return  
    # Realiza a transação de depósito na conta do cliente.
    cliente.realizar_transacao(conta, transacao) 
    # Função para realizar um saque em uma conta.
def sacar(clientes):
    # Obtém o CPF do cliente.
    cpf = input("Informe o CPF do cliente: ") 
    # Encontra o cliente na lista de clientes pelo CPF.
    cliente = filtrar_cliente(cpf, clientes)  
    # Verifica se o cliente foi encontrado.
    if not cliente:  
        # Exibe mensagem de erro se o cliente não for encontrado.
        print("\n@@@ Cliente não encontrado! @@@") 
        # Retorna se o cliente não for encontrado.
        return  
    # Obtém o valor do saque.
    valor = float(input("Informe o valor do saque: "))  
    # Cria uma transação de saque.
    transacao = Saque(valor)  
    # Recupera a conta do cliente. 
    conta = recuperar_conta_cliente(cliente)  
    # Verifica se a conta foi recuperada.
    if not conta: 
        # Retorna se a conta não for recuperada.
        return  
    # Realiza a transação de saque na conta do cliente.
    cliente.realizar_transacao(conta, transacao)  

# Função para exibir o extrato de uma conta.
def exibir_extrato(clientes):
    # Obtém o CPF do cliente. 
    cpf = input("Informe o CPF do cliente: ")  
    # Encontra o cliente na lista de clientes pelo CPF.
    cliente = filtrar_cliente(cpf, clientes)  
    # Verifica se o cliente foi encontrado.
    if not cliente:  
        # Exibe mensagem de erro se o cliente não for encontrado.
        print("\n@@@ Cliente não encontrado! @@@")  
        # Retorna se o cliente não for encontrado.
        return  
    # Recupera a conta do cliente. 
    conta = recuperar_conta_cliente(cliente) 
    # Verifica se a conta foi recuperada.
    if not conta:  
        # Retorna se a conta não for recuperada.
        return 
    # Exibe o cabeçalho do extrato.
    print("\n================ EXTRATO ================")  
    # Obtém a lista de transações da conta.
    transacoes = conta.historico.transacoes  
    # Inicializa uma string vazia para armazenar o extrato.
    extrato = ""  
    # Verifica se há transações no histórico.
    if not transacoes: 
        # Define o extrato como uma mensagem informando que não houve movimentações. 
        extrato = "Não foram realizadas movimentações."  
    else:
        # Itera sobre a lista de transações e adiciona as informações ao extrato. 
        for transacao in transacoes:  
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"  
    # Exibe o extrato. 
    print(extrato)  
    # Exibe o saldo da conta.
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")  
    # Exibe o rodapé do extrato.
    print("==========================================")  

# Função para criar um novo cliente. 
def criar_cliente(clientes):
    # Obtém o CPF do cliente.
    cpf = input("Informe o CPF (somente número): ")  
    # Verifica se já existe um cliente com o mesmo CPF.
    cliente = filtrar_cliente(cpf, clientes) 
    # Se o cliente já existir, exibe mensagem de erro e retorna.
    if cliente:  
        print("\n@@@ Já existe cliente com esse CPF! @@@")  
        return 
    # Obtém o nome do cliente.
    nome = input("Informe o nome completo: ")  
    # Obtém a data de nascimento do cliente. 
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")  
    # Obtém o endereço do cliente. 
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")  
    # Cria um novo objeto PessoaFisica com as informações do cliente. 
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco) 
    # Adiciona o novo cliente à lista de clientes.
    clientes.append(cliente) 
    # Exibe mensagem de sucesso.
    print("\n=== Cliente criado com sucesso! ===") 

# Função para criar uma nova conta para um cliente.
def criar_conta(numero_conta, clientes, contas):
    # Obtém o CPF do cliente.
    cpf = input("Informe o CPF do cliente: ")  
    # Encontra o cliente na lista de clientes pelo CPF.
    cliente = filtrar_cliente(cpf, clientes)  
    # Verifica se o cliente foi encontrado.
    if not cliente:  
        # Exibe mensagem de erro se o cliente não for encontrado. 
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")  
        # Retorna se o cliente não for encontrado.
        return  
    # Cria uma nova conta corrente para o cliente. 
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)  
    # Adiciona a nova conta à lista de contas do banco.
    contas.append(conta) 
    # Adiciona a nova conta à lista de contas do cliente. 
    cliente.contas.append(conta)  
    # Exibe mensagem de sucesso.
    print("\n=== Conta criada com sucesso! ===")  
    # Função para listar todas as contas do banco.
def listar_contas(contas):
    # Itera sobre a lista de contas e exibe as informações de cada conta.
    for conta in contas:  
        print("=" * 100)
        print(textwrap.dedent(str(conta)))  

# Função principal do programa.
def main():
    # Cria listas vazias para armazenar clientes e contas.
    clientes = []  
    contas = []  
    # Loop infinito para exibir o menu e executar as opções escolhidas pelo usuário.
    while True:  
        # Exibe o menu e obtém a opção escolhida pelo usuário.
        opcao = menu()  
        # Verifica a opção escolhida e executa a ação correspondente.
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            # Gera um número de conta com base no tamanho da lista de contas. 
            numero_conta = len(contas) + 1  
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            # Sai do loop e encerra o programa.
            break  
        else:
            # Exibe mensagem de erro se a opção for inválida.
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")  

# Inicia o programa chamando a função main.
main() 