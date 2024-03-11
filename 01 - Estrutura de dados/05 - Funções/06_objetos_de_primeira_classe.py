# Define a função 'somar', que aceita dois argumentos 'a' e 'b'.
def somar(a, b):
    # Retorna a soma dos argumentos 'a' e 'b'.
    return a + b

# Define a função 'exibir_resultado', que aceita dois números ('a' e 'b') e uma função ('funcao').
def exibir_resultado(a, b, funcao):
    # A variável 'resultado' recebe o retorno da função 'funcao', passando 'a' e 'b' como argumentos.
    resultado = funcao(a, b)

    # Imprime uma mensagem formatada com os valores de 'a', 'b' e 'resultado'.
    print(f"O resultado da operação {a} + {b} = {resultado}")

# Chama a função 'exibir_resultado', passando 10 e 10 como os números e 'somar' como a função.
# Isso imprime "O resultado da operação 10 + 10 = 20" no console.
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20


