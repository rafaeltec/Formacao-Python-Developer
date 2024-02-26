# Definição de uma tupla chamada 'carros'. Tuplas são coleções imutáveis em Python.
# Esta tupla contém três strings, cada uma representando o nome de um carro.
carros = (
    "gol",
    "celta",
    "palio",
)

# Primeiro loop 'for': Itera sobre cada elemento da tupla 'carros'.
# A variável 'carro' recebe cada elemento da tupla 'carros' a cada iteração do loop.
for carro in carros:
    # Imprime o nome do carro atual.
    print(carro)

# Segundo loop 'for': Itera sobre a tupla 'carros', mas desta vez usando a função 'enumerate'.
# 'enumerate' fornece um contador (índice) junto com o valor (carro) da tupla.
# 'indice' é o índice atual na tupla e 'carro' é o valor (nome do carro).
for indice, carro in enumerate(carros):
    # Imprime o índice e o nome do carro, formatados de maneira específica.
    # '{indice}: {carro}' é uma string formatada onde os valores de 'indice' e 'carro'
    # são inseridos nas respectivas posições.
    print(f"{indice}: {carro}") 
    #A letra f antes das aspas indica que a string é uma "f-string",
    # uma funcionalidade introduzida no Python 3.6. 
    # A f-string é uma forma de formatar strings de maneira mais eficiente e legível. 
