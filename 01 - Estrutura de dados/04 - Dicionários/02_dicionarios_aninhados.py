# Criando um dicionário chamado 'contatos'. 
# Cada chave é um e-mail e cada valor é outro dicionário contendo informações do contato.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "22930022"},
    "maria@exemplo.com": {"nome": "Maria", "telefone": "22930023"},
    "joao@exemplo.com": {"nome": "João", "telefone": "22930024"},
    "ana@exemplo.com": {"nome": "Ana", "telefone": "22930025"},
    "carlos@exemplo.com": {"nome": "Carlos", "telefone": "22930026"},
    "julia@exemplo.com": {"nome": "Júlia", "telefone": "22930027", "extra": {"a": 1}}
}

# Acessando o número de telefone de 'Maria' usando sua chave de e-mail.
# 'contatos["maria@exemplo.com"]' acessa o dicionário de Maria,
# e '["telefone"]' acessa o número de telefone dentro desse dicionário.
telefone = contatos["maria@exemplo.com"]["telefone"]
print(telefone)  # Imprime o telefone de Maria

# Acessando a informação extra da 'Júlia' que está dentro de um dicionário aninhado.
# Primeiro, acessamos o dicionário de Júlia, depois o dicionário 'extra' e, por fim, o valor associado à chave 'a'.
extra = contatos["julia@exemplo.com"]["extra"]["a"]
print(extra)  # Imprime o valor extra da Júlia

# Iterando sobre cada chave no dicionário 'contatos'.
# 'chave' representa cada e-mail (chave do dicionário) em cada iteração.
for chave in contatos:
    # Imprimindo a chave (e-mail) e o valor (dicionário de informações do contato) associados.
    print(chave, contatos[chave])


#Remove todos os itens do dicionário 'contatos'.
#Após esta linha, 'contatos' será um dicionário vazio.
#contatos.clear()

