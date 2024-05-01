T = int(input("Digite o número de casos de teste: "))

resultados = []

for i in range(T):
    # Recebe o número de garrafas compradas e a quantidade necessária para trocar por uma cheia
    N, K = map(int, input(f"Digite os valores de N e K para o caso {i+1}: ").split())
    
    # Garrafas iniciais compradas
    total_garrafas = N
    # Garrafas que podem ser trocadas
    cascos_disponiveis = N
    
    while cascos_disponiveis >= K:
        # Calcula quantas garrafas novas são obtidas pela troca dos cascos
        novas_garrafas = cascos_disponiveis // K
        # Adiciona as novas garrafas ao total
        total_garrafas += novas_garrafas
        # Calcula quantos cascos sobram depois das trocas
        cascos_disponiveis = cascos_disponiveis % K + novas_garrafas
    
    # Armazena o resultado para cada caso
    resultados.append(total_garrafas)

# Exibe os resultados
for resultado in resultados:
    print(resultado)



pelo resultado é o teu cálculo que está errado, a operação é : (N // K) + (N % K)