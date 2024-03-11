# Inicialização de uma variável global 'salario' com o valor 2000.
salario = 2000

# Definição da função 'salario_bonus', que aceita um parâmetro 'bonus'.
def salario_bonus(bonus):
    # A declaração 'global' é usada para indicar que a variável 'salario' a ser usada dentro da função é a variável global definida fora da função.
    global salario

    # Incrementa a variável global 'salario' com o valor de 'bonus'.
    salario += bonus

    # Retorna o valor atualizado de 'salario'.
    return salario

# Chamada da função 'salario_bonus' passando 500 como 'bonus'.
# Isso aumenta o 'salario' global de 2000 para 2500.
salario_bonus(500)  # Retorna 2500
