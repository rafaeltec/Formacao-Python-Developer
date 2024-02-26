# Cria um conjunto chamado 'conjunto_a' com os elementos 1, 2 e 3.
conjunto_a = {1, 2, 3}

# Cria outro conjunto chamado 'conjunto_b' com os elementos 2, 3 e 4.
conjunto_b = {2, 3, 4}

# Utiliza o método .intersection() para obter a interseção entre 'conjunto_a' e 'conjunto_b'.
# A interseção de dois conjuntos consiste nos elementos que são comuns a ambos os conjuntos.
resultado = conjunto_a.intersection(conjunto_b)

# Imprime o resultado da interseção.
# Neste caso, tanto 'conjunto_a' quanto 'conjunto_b' contêm os números 2 e 3,
# então estes serão os elementos do conjunto 'resultado'.
print(resultado)  # Saída: {2, 3}
