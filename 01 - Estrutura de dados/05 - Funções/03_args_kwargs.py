# Define a função 'exibir_poema' que aceita um argumento obrigatório 'data_extenso',
# um número variável de argumentos posicionais (*args) e um número variável de argumentos nomeados (**kwargs).
def exibir_poema(data_extenso, *args, **kwargs):
    # Junta todos os argumentos posicionais em uma única string, separados por uma quebra de linha.
    # Isso forma o corpo do poema.
    texto = "\n".join(args)

    # Cria uma lista de strings formatadas com os pares chave-valor dos argumentos nomeados.
    # Cada par é formatado como "Chave: Valor", e os elementos da lista são unidos em uma única string, separados por quebras de linha.
    # Isso forma os metadados do poema.
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])

    # Formata a mensagem final, incluindo a data (ou título), o texto do poema e os metadados.
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    # Imprime a mensagem final.
    print(mensagem)

# Chama a função 'exibir_poema' com um argumento obrigatório (que serve como título),
# vários argumentos posicionais (linhas do poema) e argumentos nomeados (metadados do poema).
exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "bla bla bla",
    "cha cha cha",
    # [linhas adicionais do poema omitidas para brevidade]
    autor="Tim Peters",
    ano=1999,
)

# args e kargs pode mudar de nome, o python olha o * e ** - pro convenção usamos args e kargs.