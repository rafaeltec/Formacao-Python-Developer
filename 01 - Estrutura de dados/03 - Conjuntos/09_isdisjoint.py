# Cria um conjunto chamado 'conjunto_a' com os elementos 1, 2, 3, 4 e 5.
conjunto_a = {1, 2, 3, 4, 5}

# Cria outro conjunto chamado 'conjunto_b' com os elementos 6, 7, 8 e 9.
conjunto_b = {6, 7, 8, 9}

# Cria um terceiro conjunto chamado 'conjunto_c' com os elementos 1 e 0.
conjunto_c = {1, 0}

# Utiliza o método .isdisjoint() para verificar se 'conjunto_a' e 'conjunto_b' são disjuntos.
# Dois conjuntos são disjuntos se não têm elementos em comum.
resultado = conjunto_a.isdisjoint(conjunto_b)
# Imprime o resultado. Será True, pois não existem elementos comuns entre 'conjunto_a' e 'conjunto_b'.
print(resultado)  # Saída: True

# Utiliza o método .isdisjoint() para verificar se 'conjunto_a' e 'conjunto_c' são disjuntos.
resultado = conjunto_a.isdisjoint(conjunto_c)
# Imprime o resultado. Será False, pois existe pelo menos um elemento comum ('1') entre 'conjunto_a' e 'conjunto_c'.
print(resultado)  # Saída: False
