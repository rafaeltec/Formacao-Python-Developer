contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Removendo a chave "telefone" do dicionário associado ao e-mail "guilherme@gmail.com".
del contatos["guilherme@gmail.com"]["telefone"]

# Removendo completamente a entrada correspondente ao e-mail "chappie@gmail.com".
del contatos["chappie@gmail.com"]

# Imprimindo o dicionário de contatos após as remoções.
print(contatos)
