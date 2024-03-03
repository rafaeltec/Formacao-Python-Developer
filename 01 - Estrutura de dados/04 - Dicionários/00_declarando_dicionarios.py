# Criando um dicionário pessoa com duas chaves: "nome" e "idade", e seus respectivos valores.
pessoa = {"nome": "Guilherme", "idade": 28}
# Imprimindo o dicionário pessoa.
print(pessoa)

# Criando um dicionário pessoa usando o construtor dict() e passando os pares chave-valor como argumentos de palavra-chave.
pessoa = dict(nome="Guilherme", idade=28)
# Imprimindo o dicionário pessoa.
print(pessoa)

# Adicionando uma nova chave "telefone" com o valor "3333-1234" ao dicionário pessoa.
pessoa["telefone"] = "3333-1234"
# Imprimindo o dicionário pessoa, agora atualizado com a nova chave "telefone".
print(pessoa)
