# Definindo uma função chamada 'calcular_total' que aceita uma lista de números como argumento
# e retorna a soma de todos os números na lista
def calcular_total(numeros):
    return sum(numeros)

# Definindo uma função chamada 'retorna_antecessor_e_sucessor' que aceita um número como argumento
# e retorna o antecessor e o sucessor desse número
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1  # Calcula o antecessor subtraindo 1 do número fornecido
    sucessor = numero + 1    # Calcula o sucessor adicionando 1 ao número fornecido
    return antecessor, sucessor  # Retorna uma tupla contendo o antecessor e o sucessor

# Chamando a função 'calcular_total' com uma lista de números [10, 20, 34]
# e imprimindo o resultado da soma desses números (64)
print(calcular_total([10, 20, 34]))

# Chamando a função 'retorna_antecessor_e_sucessor' com o número 10
# e imprimindo o antecessor (9) e o sucessor (11) separadamente
print(retorna_antecessor_e_sucessor(10))

