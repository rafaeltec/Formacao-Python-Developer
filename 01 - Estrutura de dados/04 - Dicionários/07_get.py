contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Tentativa de acesso a uma chave que não existe no dicionário (chave "chave"), resultará em KeyError.
# contatos["chave"]  # KeyError

# Usando get() para tentar acessar uma chave que não existe, resultará em None.
resultado = contatos.get("chave")
print(resultado)  # Saída: None

# Usando get() com um valor padrão (dicionário vazio {}) para tentar acessar uma chave que não existe, resultará em {}.
resultado = contatos.get("chave", {})
print(resultado)  # Saída: {}

# Usando get() para acessar uma chave que existe no dicionário.
# Neste caso, a chave é "guilherme@gmail.com" e o valor associado a essa chave é o dicionário {"nome": "Guilherme", "telefone": "3333-2221"}.
# Portanto, o resultado será o valor associado à chave.
resultado = contatos.get("guilherme@gmail.com", {})
print(resultado)  # Saída: {"nome": "Guilherme", "telefone": "3333-2221"}
