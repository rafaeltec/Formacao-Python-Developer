# Usando operador AND - todos precisam ser verdadeiros para o resultado ser True
print(True and True and True)  # True, pois todos são | True 1 and 1 and 1 =1
print(True and False and True)  # False, pois um é False | 1 and 0 and 1 =0
print(False and False and False) # False, pois todos são False | 0 and 0 and 0 =0

# Usando operador OR - apenas um precisa ser verdadeiro para o resultado ser True
print(True or True or True)  # True, pois todos são True | 1 or 1 or 1 = 1
print(True or False or False) # True, pois um é True | 1 or 0 or 0 = 1
print(False or False or False) # False, pois todos são False | 0 or 0 or 0 = 0

# Definindo variáveis para a próxima parte do código
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Verifica se o saldo é suficiente e o saque é menor ou igual ao limite, 
# ou se é uma conta especial e o saldo é suficiente.
# Nesta expressão, 'and' tem precedência sobre 'or', então a primeira parte 
# ('saldo >= saque and saque <= limite') é avaliada primeiro.
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)  # O resultado é True

# Mesma verificação, mas com parênteses para tornar a ordem de avaliação mais clara.
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)  # O resultado é True

# Divide a expressão em duas variáveis para maior clareza.
# 'conta_normal_com_saldo_suficiente' é True se o saldo for suficiente 
# e o saque não exceder o limite.
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite

# 'conta_especial_com_saldo_suficiente' é True se for uma conta especial 
# e o saldo for suficiente.
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

# Verifica se alguma das condições acima é verdadeira.
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)  # O resultado é True
