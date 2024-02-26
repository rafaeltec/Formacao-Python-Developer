# Cria um conjunto chamado 'conjunto_a' com os elementos 1, 2 e 3.
conjunto_a = {1, 2, 3}

# Cria outro conjunto chamado 'conjunto_b' com os elementos 2, 3 e 4.
conjunto_b = {2, 3, 4}

# Utiliza o método .symmetric_difference() para obter a diferença simétrica entre 'conjunto_a' e 'conjunto_b'.
# A diferença simétrica entre dois conjuntos é o conjunto de elementos que estão em um dos conjuntos,
# mas não em ambos ao mesmo tempo.
resultado = conjunto_a.symmetric_difference(conjunto_b)

# Imprime o resultado da diferença simétrica.
# Neste caso, os elementos comuns 2 e 3 são excluídos do resultado.
# O conjunto 'resultado' contém os elementos que são exclusivos de cada conjunto: 1 de 'conjunto_a' e 4 de 'conjunto_b'.
print(resultado)  # Saída: {1, 4}
