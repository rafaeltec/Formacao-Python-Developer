# Lista original de números
numeros = [1, 30, 21, 2, 9, 65, 34]

# Filtra a lista 'numeros', mantendo apenas os números pares
pares = [numero for numero in numeros if numero % 2 == 0]

# Imprime a lista de números pares
print(pares)


# Lista original de números
numeros = [1, 30, 21, 2, 9, 65, 34]

# Cria uma nova lista 'quadrado', onde cada elemento é o quadrado do elemento correspondente em 'numeros'
quadrado = [numero**2 for numero in numeros]

# Imprime a lista de números ao quadrado
print(quadrado)
