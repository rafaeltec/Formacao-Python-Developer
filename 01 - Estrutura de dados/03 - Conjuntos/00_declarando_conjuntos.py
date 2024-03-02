# Cria um conjunto chamado 'numeros'. Os conjuntos em Python são coleções não ordenadas de elementos únicos.
# Ao criar o conjunto a partir de uma lista que contém elementos repetidos, os elementos duplicados são removidos.
numeros = set([1, 2, 3, 1, 3, 4])
# Imprime o conjunto 'numeros'. 
# A saída será {1, 2, 3, 4}, pois os elementos duplicados (1 e 3) são removidos.
print(numeros)  # {1, 2, 3, 4}

# Cria um conjunto chamado 'letras' a partir de uma string "abacaxi".
# Cada caractere da string se torna um elemento do conjunto, e os duplicados são removidos.
letras = set("abacaxi")
# Imprime o conjunto 'letras'. 
# A saída será um conjunto dos caracteres únicos da string, por exemplo, {"a", "b", "c", "x", "i"}.
# A ordem pode variar, pois os conjuntos não mantêm a ordem dos elementos.
print(letras)  # {"a", "b", "c", "x", "i"}

# Cria um conjunto chamado 'carros' a partir de uma tupla que contém nomes de carros com duplicatas.
carros = set(("palio", "gol", "celta", "palio"))
# Imprime o conjunto 'carros'. 
# A saída será um conjunto com os elementos únicos da tupla, por exemplo, {"gol", "celta", "palio"}.
# Novamente, a ordem dos elementos na saída pode variar.
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python","java","python"}
print(linguagens)

