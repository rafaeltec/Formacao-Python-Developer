# Cria um conjunto chamado 'conjunto_a' com os elementos 1, 2 e 3.
conjunto_a = {1, 2, 3}

# Cria outro conjunto chamado 'conjunto_b' com os elementos 2, 3 e 4.
conjunto_b = {2, 3, 4}

# Utiliza o método .difference() para obter a diferença entre 'conjunto_a' e 'conjunto_b'.
# A diferença de conjuntos é um conjunto de elementos que estão em 'conjunto_a' mas não em 'conjunto_b'.
resultado = conjunto_a.difference(conjunto_b)
# Imprime o resultado da diferença.
# Neste caso, o elemento 1 está em 'conjunto_a' mas não em 'conjunto_b', então é o único elemento do resultado.
print(resultado)  # Saída: {1}

# Agora, calcula a diferença de 'conjunto_b' em relação a 'conjunto_a'.
resultado = conjunto_b.difference(conjunto_a)
# Imprime o resultado da diferença.
# Aqui, o elemento 4 está em 'conjunto_b' mas não em 'conjunto_a', então é o único elemento do resultado.
print(resultado)  # Saída: {4}
