# Definição da função 'salvar_carro'. Ela recebe quatro argumentos: marca, modelo, ano e placa.
def salvar_carro(marca, modelo, ano, placa):
    # Esta linha é apenas um comentário para indicar que normalmente aqui iria o código para salvar o carro no banco de dados.
    # salva carro no banco de dados...

    # Aqui, a função imprime uma mensagem formatada contendo os detalhes do carro.
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Primeira chamada da função: os argumentos são passados diretamente e na ordem definida na função.
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Segunda chamada da função: os argumentos são passados utilizando o nome dos parâmetros. Isso é útil para melhorar a legibilidade e permite passar os argumentos fora de ordem, se necessário.
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Terceira chamada da função: os argumentos são passados usando um dicionário com a desestruturação (**). 
# Isso é útil quando os dados já estão em um dicionário e você quer passá-los diretamente para a função.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
