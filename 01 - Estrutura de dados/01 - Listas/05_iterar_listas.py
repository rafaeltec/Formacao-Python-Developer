# Lista de carros
carros = ["gol", "celta", "palio"]

# Itera sobre a lista 'carros', atribuindo cada elemento à variável 'carro'
for carro in carros:
    print(carro)


# Itera sobre a lista 'carros', obtendo tanto o índice (posição) quanto o valor de cada elemento
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
