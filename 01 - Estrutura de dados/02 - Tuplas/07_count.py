# Cria uma tupla chamada 'cores'. Tuplas são coleções ordenadas e imutáveis.
# Esta tupla contém quatro strings, cada uma representando uma cor.
cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

# Utiliza o método .count() na tupla 'cores' para contar quantas vezes
# a string "vermelho" aparece na tupla.
print(cores.count("vermelho"))  # Resultado: 1

# Conta quantas vezes a string "azul" aparece na tupla.
# Como "azul" aparece duas vezes, o resultado será 2.
print(cores.count("azul"))  # Resultado: 2

# Conta quantas vezes a string "verde" aparece na tupla.
# "verde" aparece apenas uma vez, portanto, o resultado será 1.
print(cores.count("verde"))  # Resultado: 1
