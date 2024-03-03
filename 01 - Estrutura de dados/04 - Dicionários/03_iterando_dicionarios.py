# Definindo o dicionário de contatos, onde as chaves são os endereços de e-mail e os valores são dicionários com informações sobre cada contato.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Iterando sobre o dicionário de contatos e imprimindo as chaves (endereços de e-mail) e os valores (informações do contato).
for chave in contatos:
    print(chave, contatos[chave])

# Imprimindo um separador para melhorar a visualização.
print("=" * 100)

# Iterando sobre o dicionário de contatos usando o método items(), que retorna pares (chave, valor), e imprimindo cada par.
for chave, valor in contatos.items():
    print(chave, valor)
