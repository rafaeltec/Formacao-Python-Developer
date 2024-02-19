# Define a função 'sacar' que recebe um valor como argumento.
def sacar(valor):
    # Define uma variável local 'saldo' e atribui a ela o valor 500.
    saldo = 500

    # Verifica se o saldo é suficiente para o saque.
    if saldo >= valor:
        # Se o saldo for suficiente, imprime mensagens indicando o sucesso do saque.
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    # Imprime uma mensagem de agradecimento, que é exibida independentemente do resultado do saque.
    print("Obrigado por ser nosso cliente, tenha um bom dia!")


# Define a função 'depositar' que recebe um valor como argumento.
def depositar(valor):
    # Define uma variável local 'saldo' e atribui a ela o valor 500.
    saldo = 500
    # Adiciona o valor do depósito ao saldo.
    saldo += valor

# Chama a função 'sacar' com o valor de 1000.
sacar(1000)


""""
Em Python, a palavra-chave def é usada para definir uma função. A função é um bloco de código que só é executado quando é chamada. Você pode passar dados,
conhecidos como parâmetros, para uma função. Uma função pode retornar dados como resultado. A sintaxe básica para definir uma função em Python é a seguinte:

def nome_da_funcao(parametros):
    # bloco de código da função

def informa ao Python que você está definindo uma função.
nome_da_funcao é o nome que você dá à função. Você usa este nome para chamar a função mais tarde.
parametros são os valores que você pode passar para a função. Eles são opcionais; uma função pode ter nenhum, um ou vários parâmetros.
O # bloco de código da função é onde você escreve o código que define o que a função faz.

"""

def saudar(nome):
    print("Olá, " + nome + "!")

saudar("Maria")

