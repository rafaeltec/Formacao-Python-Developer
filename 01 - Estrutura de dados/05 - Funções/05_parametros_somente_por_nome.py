# Definição da função 'criar_carro'.
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    # Os parâmetros antes da '/' são positional-only, ou seja, devem ser fornecidos
    # apenas como argumentos posicionais e não podem ser chamados pelo nome.

    # Os parâmetros depois do '*' são keyword-only, ou seja, devem ser fornecidos
    # com seus nomes explicitamente e não podem ser passados como argumentos posicionais.

    # Imprime os valores dos parâmetros.
    print(modelo, ano, placa, marca, motor, combustivel)

# Chamada válida da função 'criar_carro'.
# Os primeiros três argumentos são passados posicionalmente (conforme exigido).
# Os três últimos argumentos são passados usando seus nomes (conforme exigido).
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Chamada inválida da função 'criar_carro'.
# Esta linha resultará em erro, pois os primeiros três argumentos não podem ser passados com seus nomes.
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
