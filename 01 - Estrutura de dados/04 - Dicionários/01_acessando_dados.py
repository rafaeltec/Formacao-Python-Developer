# Criando um dicionário chamado dados contendo informações sobre uma pessoa.
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# Imprimindo o valor associado à chave "nome" no dicionário dados.
print(dados["nome"])  # "Guilherme"
# Imprimindo o valor associado à chave "idade" no dicionário dados.
print(dados["idade"])  # 28
# Imprimindo o valor associado à chave "telefone" no dicionário dados.
print(dados["telefone"])  # "3333-1234"

# Atualizando o valor associado à chave "nome" no dicionário dados para "Maria".
dados["nome"] = "Maria"
# Atualizando o valor associado à chave "idade" no dicionário dados para 18.
dados["idade"] = 18
# Atualizando o valor associado à chave "telefone" no dicionário dados para "9988-1781".
dados["telefone"] = "9988-1781"

# Imprimindo o dicionário dados, agora com os valores atualizados.
print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}








#MANEIRA CLASSICA:
# Criando um dicionário diretamente com os valores definidos.
dados = dict(nome="Guilherme", idade=28, telefone="3333-1234")
#dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"} mesma coisa, mais simples
# Imprimindo os valores associados a cada chave.
print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

# Atualizando os valores no dicionário.
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

# Imprimindo o dicionário completo após a atualização.
print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
