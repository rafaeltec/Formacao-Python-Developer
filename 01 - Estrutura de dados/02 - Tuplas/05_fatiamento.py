
# Define uma tupla chamada 'tupla' contendo letras individuais.
objeto = ("p", "y", "t", "h", "o", "n",) # a virgula no final indica uma tupla

# Imprime a tupla a partir do terceiro elemento até o final.
# tupla[2:] começa do índice 2 (terceiro elemento) e vai até o final da tupla.
print(objeto[2:])  # ("t", "h", "o", "n")

# Imprime os primeiros dois elementos da tupla.
# tupla[:2] começa do início da tupla e vai até o índice 2, sem incluí-lo.
print(objeto[:2])  # ("p", "y")

# Imprime os elementos da tupla do índice 1 até 3, sem incluir o índice 3.
# tupla[1:3] começa do índice 1 e vai até o índice 3, sem incluí-lo.
print(objeto[1:3])  # ("y", "t")

# Imprime os elementos da tupla do índice 0 até 3, com passos de 2.
# tupla[0:3:2] começa do índice 0, vai até o índice 3, sem incluí-lo, pulando de dois em dois.
print(objeto[0:3:2])  # ("p", "t")

# Imprime todos os elementos da tupla.
# tupla[::] copia a tupla inteira.
print(objeto[::])  # ("p", "y", "t", "h", "o", "n")

# Imprime todos os elementos da tupla em ordem inversa.
# tupla[::-1] inverte a ordem da tupla.
print(objeto[::-1])  # ("n", "o", "h", "t", "y", "p")


objeto2 = tuple("p" "y" "t" "h" "o" "n") # tupla da forma tradicional os textos "Rafael" "carlos" nao sao sep por virgula
# Imprime a tupla 'numeros'.
print(objeto2)
