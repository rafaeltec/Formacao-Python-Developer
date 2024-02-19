# Cria uma lista chamada 'frutas' contendo os elementos "limao" e "uva".
frutas = ["limao", "uva"]

# Cria uma string 'curso' com o conteúdo "Curso de python".
curso = "Curso de python"

# Verifica se a string "laranja" não está presente na lista 'frutas'. 
# Retorna True se "laranja" não estiver na lista, False caso contrário.
print("laranja" not in frutas)

# Verifica se a string "limao" está presente na lista 'frutas'.
# Retorna True se "limao" estiver na lista, False caso contrário.
print("limao" in frutas)

# Verifica se a string "Python" está presente na string 'curso'.
# Importante: a verificação é sensível a maiúsculas e minúsculas. 
# Retorna True se "Python" for encontrado exatamente como está, False caso contrário.
# Neste caso, retornará False porque "Python" não é igual a "python" (diferença de maiúsculas/minúsculas).
print("Python" in curso)
