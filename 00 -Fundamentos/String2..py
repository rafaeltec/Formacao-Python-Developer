nome = "Rafael"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.4512345674

dados = {"nome": "Rafael", "idade": 28}

print("nome: %s idade: %d" % (nome, idade))

print("nome: {} idade{}".format(nome, idade))

print("nome:{1} idade{0}".format(idade, nome))
print("nome:{1} idade{0} nome:{1}{1}".format(idade, nome))


print("nome: {nome} idade:{idade}" .format(nome=nome, idade=idade))
print("nome: {name} idade:{age} {name} {name} {age}".format (age=idade, name=nome))
print("nome:{nome} idade:{idade}".format(**dados))

print(f"nome:{nome} idade:{idade}")
print(f"nome:{nome} idade:{idade} saldo: {saldo:.6f}")
print(f"nome:{nome} idade:{idade} saldo: {saldo:10.2f}")