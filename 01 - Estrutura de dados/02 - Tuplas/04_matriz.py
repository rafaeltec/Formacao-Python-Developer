# Cria uma matriz (uma tupla de tuplas) chamada 'matriz'.
# Cada tupla interna representa uma linha da matriz.
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

# Imprime a primeira linha da matriz.
# matriz[0] acessa a primeira tupla dentro da tupla 'matriz'.
print(matriz[0])  # (1, "a", 2)

# Imprime o primeiro elemento da primeira linha da matriz.
# matriz[0][0] acessa o primeiro elemento da primeira tupla.
print(matriz[0][0])  # 1

# Imprime o último elemento da primeira linha da matriz usando indexação negativa.
# matriz[0][-1] acessa o último elemento da primeira tupla.
print(matriz[0][-1])  # 2

# Imprime o último elemento da última linha da matriz, também usando indexação negativa.
# matriz[-1] acessa a última tupla, e [-1] acessa o último elemento dessa tupla.
print(matriz[-1][-1])  # "c"

print(matriz[1][1])  # 3 lembrando que da esquerda para direita começa em ZERO !
                     # da direita para esquerda começa em 1 !
                     