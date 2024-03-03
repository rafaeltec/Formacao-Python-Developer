# Criando um dicionário contatos com um único contato.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Fazendo uma cópia do dicionário contatos.
copia = contatos.copy()

# Modificando o valor associado à chave "guilherme@gmail.com" na cópia.
copia["guilherme@gmail.com"] = {"nome": "Gui"}

# Imprimindo o valor associado à chave "guilherme@gmail.com" no dicionário original contatos.
print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

# Imprimindo o valor associado à chave "guilherme@gmail.com" na cópia.
print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
