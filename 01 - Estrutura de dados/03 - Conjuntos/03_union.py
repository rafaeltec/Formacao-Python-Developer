# Cria dois conjuntos, 'conjunto_a' e 'conjunto_b'.
# 'conjunto_a' contém os números 1 e 2, enquanto 'conjunto_b' contém os números 3 e 4.
conjunto_a = {1, 2}
conjunto_b = {3, 4}

# Une os dois conjuntos usando o método 'union'.
# O método 'union' retorna um novo conjunto que contém todos os elementos que estão em 'conjunto_a' 
# ou em 'conjunto_b', ou em ambos.
resultado = conjunto_a.union(conjunto_b)

# Imprime o conjunto resultante da união.
# O resultado será um conjunto contendo os números {1, 2, 3, 4}.
print(resultado)
