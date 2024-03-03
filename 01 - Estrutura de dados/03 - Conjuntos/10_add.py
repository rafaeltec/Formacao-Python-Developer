# Criação de um conjunto chamado 'sorteio' com dois elementos: 1 e 23.
sorteio = {1, 23}

# Adiciona o número 25 ao conjunto 'sorteio'. 
# Conjuntos não permitem elementos duplicados, então 25 só será adicionado uma vez.
sorteio.add(25)  # Após esta linha, 'sorteio' será {1, 23, 25}
print(sorteio)

# Adiciona o número 42 ao conjunto 'sorteio'.
sorteio.add(42)  # Agora, 'sorteio' será {1, 23, 25, 42}
print(sorteio)

# Tenta adicionar novamente o número 25 ao conjunto 'sorteio'.
# Como 25 já está no conjunto, esta operação não terá efeito.
sorteio.add(25)  # 'sorteio' continua sendo {1, 23, 25, 42}
print(sorteio)
