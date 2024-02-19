# Inicializa uma lista vazia chamada 'lista'
lista = []

# Adiciona o número inteiro 1 ao final da lista 'lista' utilizando o método append
# Após essa operação, a lista será [1]
lista.append(1)

# Adiciona a string "Python" ao final da lista 'lista'
# Após essa operação, a lista será [1, "Python"]
lista.append("Python")

# Adiciona uma lista [40, 30, 20] como um único elemento ao final da lista 'lista'
# Após essa operação, a lista será [1, "Python", [40, 30, 20]]
# Note que a lista [40, 30, 20] é tratada como um único elemento dentro da lista 'lista'
lista.append([40, 30, 20])

# Imprime o conteúdo atual da lista 'lista', que agora contém três elementos
# O resultado impresso será [1, "Python", [40, 30, 20]]
print(lista)  # [1, "Python", [40, 30, 20]]

#first in last out, conceito de pilha
lista.append("rafael")
print(lista)