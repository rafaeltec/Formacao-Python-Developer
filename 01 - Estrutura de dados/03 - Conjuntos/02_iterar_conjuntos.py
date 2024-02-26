# Cria um conjunto chamado 'carros' contendo três strings, cada uma representando um modelo de carro.
carros = {"gol", "celta", "palio"}

# Primeiro loop 'for': percorre cada elemento do conjunto 'carros'.
# A variável 'carro' recebe cada elemento do conjunto 'carros' a cada iteração do loop.
for carro in carros:
    # Imprime o nome do carro atual.
    print(carro)

# Segundo loop 'for': utiliza a função 'enumerate' para iterar sobre o conjunto 'carros'.
# 'enumerate' fornece um par de valores a cada iteração: um índice (começando de 0) e o valor (carro).
for indice, carro in enumerate(carros):
    # Imprime o índice e o nome do carro, formatados de maneira específica.
    # '{indice}: {carro}' é uma string formatada onde os valores de 'indice' e 'carro'
    # são inseridos nas respectivas posições.
    print(f"{indice}: {carro}")
