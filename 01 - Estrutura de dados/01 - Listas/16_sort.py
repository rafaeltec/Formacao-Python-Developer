# Cria uma lista de linguagens de programação.
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista 'linguagens' em ordem alfabética.
linguagens.sort()

# Imprime a lista ordenada.
# Resultado esperado: ["c", "csharp", "java", "js", "python"]
print(linguagens)




# Cria novamente a lista de linguagens de programação.
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista 'linguagens' em ordem alfabética reversa (do Z ao A).
linguagens.sort(reverse=True)

# Imprime a lista ordenada de forma reversa.
# Resultado esperado: ["python", "js", "java", "csharp", "c"]
print(linguagens)



# Cria a lista de linguagens novamente.
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista 'linguagens' com base no comprimento de cada string.
# A função lambda 'x: len(x)' é usada como chave de ordenação.
linguagens.sort(key=lambda x: len(x))

# Imprime a lista ordenada por comprimento.
# Resultado esperado: ["c", "js", "java", "python", "csharp"]
print(linguagens)






# Cria a lista de linguagens mais uma vez.
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista 'linguagens' com base no comprimento de cada string, mas de forma reversa.
# Ou seja, das strings mais longas para as mais curtas.
linguagens.sort(key=lambda x: len(x), reverse=True)

# Imprime a lista ordenada por comprimento de forma reversa.
# Resultado esperado: ["python", "csharp", "java", "js", "c"]
print(linguagens)
