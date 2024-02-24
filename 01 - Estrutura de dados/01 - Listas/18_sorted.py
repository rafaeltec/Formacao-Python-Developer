# Cria uma lista de linguagens de programação.
linguagens = ["python", "js", "c", "java", "csharp"]

# Usa a função 'sorted()' para ordenar a lista 'linguagens'.
# A chave de ordenação ('key') é definida pela função lambda que retorna o comprimento da string (len(x)).
# Isso resulta na ordenação das linguagens do menor nome para o maior nome.
print(sorted(linguagens, key=lambda x: len(x)))
# Saída esperada: ["c", "js", "java", "python", "csharp"]







# Usa novamente a função 'sorted()' para ordenar a lista 'linguagens'.
# Desta vez, o parâmetro 'reverse=True' é adicionado para inverter a ordem da ordenação.
# Assim, a lista é ordenada do nome mais longo para o mais curto.
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
# Saída esperada: ["python", "csharp", "java", "js", "c"]
