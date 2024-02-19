# Menu de opções exibido para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# Inicializa o saldo da conta com 0
saldo = 0

# Define o limite máximo para saques individuais
limite = 500

# Inicializa a string que vai armazenar o histórico de transações para o extrato
extrato = ""

# Contador para o número de saques realizados
numero_saques = 0

# Define o limite máximo de saques permitidos
LIMITE_SAQUES = 3

# Loop infinito para manter o programa em execução
while True:

    # Solicita a opção do usuário e armazena na variável 'opcao'
    opcao = input(menu)

    # Verifica se a opção escolhida é 'd' para depósito
    if opcao == "d":
        # Pede ao usuário o valor do depósito e converte para float
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor do depósito é válido (maior que zero)
        if valor > 0:
            # Adiciona o valor ao saldo
            saldo += valor
            # Registra a operação no extrato
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            # Mensagem de erro se o valor do depósito for inválido
            print("Operação falhou! O valor informado é inválido.")

    # Verifica se a opção escolhida é 's' para saque
    elif opcao == "s":
        # Pede ao usuário o valor do saque e converte para float
        valor = float(input("Informe o valor do saque: "))

        # Verifica se o valor do saque excede o saldo, o limite de saque ou o número de saques
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Condições para validar ou recusar o saque
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            # Realiza o saque se todas as condições forem atendidas
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Verifica se a opção escolhida é 'e' para extrato
    elif opcao == "e":
        # Imprime o extrato das operações realizadas
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Verifica se a opção escolhida é 'q' para sair do programa
    elif opcao == "q":
        break

    # Mensagem de erro se uma opção inválida for escolhida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
