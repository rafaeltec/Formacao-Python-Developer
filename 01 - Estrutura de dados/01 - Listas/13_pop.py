# Cria uma lista chamada 'linguagens' com cinco elementos
linguagens = ["python", "js", "c", "java", "csharp"]

# Remove e retorna o último elemento da lista 'linguagens', que é "csharp"
print(linguagens.pop())  # Saída esperada: csharp

# Agora, o último elemento da lista atualizada é "java", que é removido e retornado
print(linguagens.pop())  # Saída esperada: java

# Novamente, o último elemento da lista agora é "c", que é removido e retornado
print(linguagens.pop())  # Saída esperada: c

# Remove e retorna o elemento no índice 0 da lista, que é "python"
print(linguagens.pop(0))  # Saída esperada: python
