# Definindo a primeira função chamada 'exibir_mensagem' que imprime uma mensagem simples
def exibir_mensagem():
    print("Olá mundo!")


# Definindo a segunda função chamada 'exibir_mensagem_2' que aceita um argumento 'nome'
# e imprime uma mensagem de boas-vindas personalizada com o nome fornecido
def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}!")


# Definindo a terceira função chamada 'exibir_mensagem_3' que aceita um argumento opcional 'nome'
# e imprime uma mensagem de boas-vindas personalizada com o nome fornecido ou "Anônimo" se nenhum nome for fornecido
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem-vindo {nome}!")


# Chamando a função 'exibir_mensagem' que imprime a mensagem "Olá mundo!"
exibir_mensagem()

# Chamando a função 'exibir_mensagem_2' com o argumento 'nome="Guilherme"'
# que imprime a mensagem "Seja bem-vindo Guilherme!"
exibir_mensagem_2(nome="Guilherme")

# Chamando a função 'exibir_mensagem_3' sem argumentos,
# que imprime a mensagem padrão "Seja bem-vindo Anônimo!"
exibir_mensagem_3()

# Chamando a função 'exibir_mensagem_3' com o argumento 'nome="Chappie"',
# que imprime a mensagem personalizada "Seja bem-vindo Chappie!"
exibir_mensagem_3(nome="Chappie")
