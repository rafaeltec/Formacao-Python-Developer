# Solicita o número de casos de teste
C = int(input("Digite o número de casos de teste: "))

# Itera sobre o número de casos de teste
for _ in range(C):
    # Lê o nível de energia de cada ser vivo
    N = int(input("Digite o nível de energia do ser vivo: "))
    
    # Avalia se o nível de energia é maior que 8000
    if N > 8000:
        print("Mais de 8000!")  # Se maior que 8000, imprime "Mais de 8000!"
    else:
        print("Inseto!")  # Se menor ou igual a 8000, imprime "Inseto!"
