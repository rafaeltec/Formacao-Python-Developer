# Cria uma tupla chamada 'linguagens'. As tuplas são coleções ordenadas e imutáveis em Python.
# Esta tupla contém cinco strings, cada uma representando o nome de uma linguagem de programação.
linguagens = ("python", "js", "c", "java", "csharp",)

# Utiliza o método .index() na tupla 'linguagens' para encontrar o índice (posição)
# da string "java". Como "java" é o quarto item na tupla (contando do zero),
# o resultado impresso será 3.
print(linguagens.index("java"))  # Resultado: 3

# Utiliza o método .index() para encontrar o índice da string "python".
# "python" é o primeiro item na tupla, então seu índice é 0.
print(linguagens.index("python"))  # Resultado: 0
