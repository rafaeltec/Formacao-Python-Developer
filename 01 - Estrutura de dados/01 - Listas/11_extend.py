# Cria uma lista chamada 'linguagens' com três elementos: "python", "js" e "c"
linguagens = ["python", "js", "c"]

# Imprime a lista 'linguagens' como ela está atualmente
print(linguagens)  # Saída esperada: ["python", "js", "c"]

# Utiliza o método extend() para adicionar dois novos elementos, "java" e "csharp", ao final da lista 'linguagens'
# Após esta operação, a lista 'linguagens' contém cinco elementos
linguagens.extend(["java", "csharp"])

# Imprime a lista 'linguagens' após a adição dos novos elementos
print(linguagens)  # Saída esperada: ["python", "js", "c", "java", "csharp"]
