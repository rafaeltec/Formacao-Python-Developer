# Definindo uma matriz com 3 linhas e diferentes números de colunas em cada linha
matriz = [
    [1, "a,2"],
    ["b", 5, "c"],
    [6, 5, "c"]
]

# Imprime a primeira linha da matriz
print(matriz[0])  # [1, "a,2"]

# Imprime o primeiro elemento da primeira linha da matriz
print(matriz[0][0])  # 1

# Imprime o último elemento da primeira linha da matriz
print(matriz[0][-1])  # "a,2"

# Imprime o último elemento da última linha da matriz
print(matriz[-1][-1])  # "c"
