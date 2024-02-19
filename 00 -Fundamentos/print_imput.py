# Solicita ao usuário que insira seu nome e armazena o valor na variável 'nome'.
nome = input("Informe o seu nome: ")

# Solicita ao usuário que insira sua idade e armazena o valor na variável 'idade'.
idade = input("Informe a sua idade: ")

# Imprime os valores de 'nome' e 'idade'. Por padrão, 'print' separa os argumentos por um espaço.
print(nome, idade)

# Imprime os valores de 'nome' e 'idade', e adiciona "..." no final, seguido por uma nova linha ('\n').
# O argumento 'end' substitui o padrão de terminação de linha (que é apenas '\n') por "...\n".
print(nome, idade, end="...\n")

# Imprime os valores de 'nome' e 'idade', separados pelo símbolo '#'.
# O argumento 'sep' substitui o separador padrão (espaço) pelo '#'.
# Ao final, adiciona "..." e uma nova linha, como no comando anterior.
print(nome, idade, sep="#", end="...\n")

# Imprime os valores de 'nome' e 'idade', separados pelo símbolo '#'.
# Diferente dos comandos anteriores, usa apenas o argumento 'sep', 
# mantendo o padrão de terminação de linha (uma nova linha '\n').
print(nome, idade, sep="#")
