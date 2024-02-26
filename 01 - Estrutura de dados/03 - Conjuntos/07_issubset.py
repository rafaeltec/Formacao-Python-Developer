# Cria um conjunto chamado 'conjunto_a' com os elementos 1, 2 e 3.
conjunto_a = {1, 2, 3}

# Cria outro conjunto chamado 'conjunto_b' que inclui elementos adicionais além dos que estão em 'conjunto_a'.
conjunto_b = {4, 1, 2, 5, 6, 3}

# Utiliza o método .issubset() para verificar se 'conjunto_a' é um subconjunto de 'conjunto_b'.
# Um conjunto A é um subconjunto de um conjunto B se todos os elementos de A também estão em B.
resultado = conjunto_a.issubset(conjunto_b)
# Imprime o resultado. Neste caso, será True, pois todos os elementos de 'conjunto_a' estão em 'conjunto_b'.
print(resultado)  # Saída: True

# Utiliza o método .issubset() para verificar se 'conjunto_b' é um subconjunto de 'conjunto_a'.
resultado = conjunto_b.issubset(conjunto_a)
# Imprime o resultado. Neste caso, será False, pois 'conjunto_b' contém elementos que não estão em 'conjunto_a'.
print(resultado)  # Saída: False

# RESUMINDO ESTÁ CONTIDO OU NÃO ESTÁ CONTIDO