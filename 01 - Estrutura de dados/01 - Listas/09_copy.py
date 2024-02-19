# Cria uma lista chamada 'lista' com um inteiro, uma string e outra lista como elementos
lista = [1, "Python", [40, 30, 20]]

# Realiza uma cópia da lista 'lista'. No entanto, essa cópia não é atribuída a nenhuma variável.
# Portanto, a cópia não é armazenada ou utilizada.
lista.copy()

# Imprime a lista original 'lista'. 
# Como a cópia anterior não foi armazenada, isso não afeta a saída desta linha de código.
print(lista)  # Saída esperada: [1, "Python", [40, 30, 20]]


copia_lista = lista.copy()
