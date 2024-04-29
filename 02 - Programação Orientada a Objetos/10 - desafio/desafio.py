# Definição do menu de opções para o usuário.
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicialização de variáveis importantes para o sistema bancário.
saldo = 0  # Saldo inicial do usuário.
limite = 500  # Limite máximo para saque individual.
extrato = ""  # String para armazenar o histórico das transações.
numero_saques = 0  # Contador de saques realizados.
LIMITE_SAQUES = 3  # Limite máximo de saques permitidos.

# Loop principal para interação do usuário com o sistema.
while True:
    opcao = input(menu)  # Apresenta o menu e captura a opção do usuário.

    # Verifica se a opção escolhida foi depositar.
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))  # Solicita o valor a ser depositado.
        if valor > 0:
            saldo += valor  # Adiciona o valor ao saldo.
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra a operação no extrato.
        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro para valor inválido.

    # Verifica se a opção escolhida foi sacar.
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))  # Solicita o valor a ser sacado.
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor  # Subtrai o valor do saldo.
            extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona o saque ao extrato.
            numero_saques += 1  # Incrementa o contador de saques.

    # Verifica se a opção escolhida foi visualizar o extrato.
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Verifica se a opção escolhida foi sair do programa.
    elif opcao == "q":
        break  # Sai do loop e termina o programa.

    else:
        # Mensagem para quando uma opção inválida é escolhida.
        print("Operação inválida, por favor selecione novamente a operação desejada.")
