# Definição da função 'criar_carro'.
# 'modelo', 'ano', e 'placa' são argumentos posicionais apenas,
# o que significa que devem ser passados sem o uso de um nome de argumento.
# 'marca', 'motor', e 'combustivel' são argumentos nomeados.
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): #modelo hibrido, usando (* e /) 
    # A função simplesmente imprime os valores passados para ela.
    print(modelo, ano, placa, marca, motor, combustivel)

# Chamada válida da função. Os primeiros três argumentos são passados posicionalmente,
# enquanto os três últimos são passados como argumentos nomeados.
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


# Chamada inválida da função. Os argumentos antes da barra ('/') não podem ser nomeados.
# Isso resultará em um erro, pois 'modelo', 'ano', e 'placa' devem ser passados posicionalmente.

'''
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
'''