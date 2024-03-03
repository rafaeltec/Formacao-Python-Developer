# Criando um dicionário
meu_dicionario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando um valor
print(meu_dicionario["nome"])  # Saída: João

# Modificando um valor
meu_dicionario["idade"] = 31

# Adicionando um novo par chave-valor
meu_dicionario["profissão"] = "Engenheiro"

# Removendo um par chave-valor
del meu_dicionario["cidade"]

print(meu_dicionario)  # Saída: {'nome': 'João', 'idade': 31, 'profissão': 'Engenheiro'}
