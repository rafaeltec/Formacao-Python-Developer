# Define a lista com os caracteres da palavra "python"
lista = ["p", "y", "t", "h", "o", "n"]

# Imprime elementos da lista a partir do índice 2 até o final
print(lista[2:])  # ["t", "h", "o", "n"]

# Imprime os primeiros dois elementos da lista (índices 0 e 1)
print(lista[:2])  # ["p", "y"]

# Imprime os elementos da lista do índice 1 até o índice 2 (não inclui o índice 3)
print(lista[1:3])  # ["y", "t"]

# Imprime os elementos da lista do índice 0 até o índice 3, pulando a cada 2 elementos
print(lista[0:3:2])  # ["p", "t"]

# Imprime todos os elementos da lista (cópia completa da lista)
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

# Imprime todos os elementos da lista em ordem reversa
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
