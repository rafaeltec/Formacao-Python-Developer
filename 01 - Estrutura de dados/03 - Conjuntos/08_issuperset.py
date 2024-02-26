# Cria um conjunto chamado 'conjunto_a' com os elementos 1, 2 e 3.
conjunto_a = {1, 2, 3}

# Cria outro conjunto chamado 'conjunto_b' que inclui alguns elementos que estão em 'conjunto_a', além de outros.
conjunto_b = {4, 1, 2, 5, 6, 3}

# Utiliza o método .issuperset() para verificar se 'conjunto_a' é um superconjunto de 'conjunto_b'.
# Um conjunto A é um superconjunto de um conjunto B se A contém todos os elementos de B.
resultado = conjunto_a.issuperset(conjunto_b)
# Imprime o resultado. Neste caso, será False, pois 'conjunto_a' não contém todos os elementos de 'conjunto_b'.
print(resultado)  # Saída: False

# Utiliza o método .issuperset() para verificar se 'conjunto_b' é um superconjunto de 'conjunto_a'.
resultado = conjunto_b.issuperset(conjunto_a)
# Imprime o resultado. Neste caso, será True, pois 'conjunto_b' contém todos os elementos de 'conjunto_a'.
print(resultado)  # Saída: True

# RESUMINDO ESTÁ CONTIDO OU NÃO ESTÁ CONTIDO